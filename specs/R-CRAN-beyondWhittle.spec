%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  beyondWhittle
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spectral Inference for Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ltsa >= 1.4.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-ltsa >= 1.4.6
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-forecast 

%description
Implementations of Bayesian parametric, nonparametric and semiparametric
procedures for univariate and multivariate time series. The package is
based on the methods presented in C. Kirch et al (2018)
<doi:10.1214/18-BA1126>, A. Meier (2018)
<https://opendata.uni-halle.de//handle/1981185920/13470> and Y. Tang et al
(2023) <doi:10.48550/arXiv.2303.11561>. It was supported by DFG grants KI
1443/3-1 and KI 1443/3-2.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
