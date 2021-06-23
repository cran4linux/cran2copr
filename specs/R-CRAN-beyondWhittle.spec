%global __brp_check_rpaths %{nil}
%global packname  beyondWhittle
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Spectral Inference for Stationary Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ltsa >= 1.4.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MTS 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-ltsa >= 1.4.6
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-MASS 
Requires:         R-CRAN-MTS 
Requires:         R-CRAN-forecast 

%description
Implementations of Bayesian parametric, nonparametric and semiparametric
procedures for univariate and multivariate time series. The package is
based on the methods presented in C. Kirch et al (2018)
<doi:10.1214/18-BA1126> and A. Meier (2018)
<https://opendata.uni-halle.de//handle/1981185920/13470>. It was supported
by DFG grant KI 1443/3-1.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
