%global packname  nearfar
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Near-Far Matching

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nbpMatching 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats 
Requires:         R-CRAN-nbpMatching 
Requires:         R-CRAN-GenSA 
Requires:         R-MASS 
Requires:         R-CRAN-car 
Requires:         R-stats 

%description
Near-far matching is a study design technique for preprocessing
observational data to mimic a pair-randomized trial. Individuals are
matched to be near on measured confounders and far on levels of an
instrumental variable.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
