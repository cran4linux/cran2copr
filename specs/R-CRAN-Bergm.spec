%global packname  Bergm
%global packver   5.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.0
Release:          1%{?dist}
Summary:          Bayesian Exponential Random Graph Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-network 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-MCMCpack 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 

%description
Bayesian analysis for exponential random graph models using advanced
computational algorithms. More information can be found at:
<https://acaimo.github.io/Bergm>.

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
