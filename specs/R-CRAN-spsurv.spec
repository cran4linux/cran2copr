%global packname  spsurv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Bernstein Polynomial Based Semiparametric Survival Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-MASS >= 7.3.51.4
BuildRequires:    R-survival >= 2.44.1.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-loo >= 2.1.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-coda >= 0.19.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
Requires:         R-MASS >= 7.3.51.4
Requires:         R-survival >= 2.44.1.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-loo >= 2.1.0
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-coda >= 0.19.3
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 

%description
A set of reliable routines to ease semiparametric survival regression
modeling based on Bernstein polynomials. 'spsurv' includes proportional
hazards, proportional odds and accelerated failure time frameworks for
right-censored data. RV Panaro (2020) <arXiv:2003.10548>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/stan
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
