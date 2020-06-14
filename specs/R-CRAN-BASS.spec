%global packname  BASS
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Bayesian Adaptive Spline Surfaces

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-gsl 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-gsl 

%description
Bayesian fitting and sensitivity analysis methods for adaptive spline
surfaces. Built to handle continuous and categorical inputs as well as
functional or scalar output. An extension of the methodology in Denison,
Mallick and Smith (1998) <doi:10.1023/A:1008824606259>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples.R
%doc %{rlibdir}/%{packname}/examplesPCA.R
%doc %{rlibdir}/%{packname}/testf1.R
%doc %{rlibdir}/%{packname}/testf2.R
%doc %{rlibdir}/%{packname}/testf3.R
%doc %{rlibdir}/%{packname}/testf4.R
%doc %{rlibdir}/%{packname}/testf5.R
%{rlibdir}/%{packname}/INDEX
