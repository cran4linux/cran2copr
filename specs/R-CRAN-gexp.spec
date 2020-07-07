%global packname  gexp
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Generator of Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-mvtnorm 
Requires:         R-tcltk 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 

%description
Generates experiments - simulating structured or experimental data as:
completely randomized design, randomized block design, latin square
design, factorial and split-plot experiments (Ferreira, 2008,
ISBN:8587692526; Naes et al., 2007 <doi:10.1002/qre.841>; Rencher et al.,
2007, ISBN:9780471754985; Montgomery, 2001, ISBN:0471316490).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/biblio
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/video
%{rlibdir}/%{packname}/INDEX
