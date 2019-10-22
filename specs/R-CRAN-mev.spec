%global packname  mev
%global packver   1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12
Release:          1%{?dist}
Summary:          Multivariate Extreme Value Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-nloptr >= 1.2.0
BuildRequires:    R-CRAN-TruncatedNormal >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-nloptr >= 1.2.0
Requires:         R-CRAN-TruncatedNormal >= 1.1
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-alabama 
Requires:         R-boot 
Requires:         R-CRAN-evd 
Requires:         R-methods 
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 

%description
Exact simulation from max-stable processes, R-Pareto processes for various
parametric models. Threshold selection methods. Multivariate extreme
diagnostics. Estimation and likelihoods for univariate extremes.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
