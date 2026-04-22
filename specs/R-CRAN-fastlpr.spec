%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastlpr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Local Polynomial Regression and Kernel Density Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Non-Uniform Fast Fourier Transform ('NUFFT')-accelerated local polynomial
regression and kernel density estimation for large, scattered, or
complex-valued datasets. Provides automatic bandwidth selection via
Generalized Cross-Validation (GCV) for regression and Likelihood
Cross-Validation (LCV) for density estimation. This is the 'R' port of the
'fastLPR' 'MATLAB'/'Python' toolbox, achieving O(N + M log M)
computational complexity through custom 'NUFFT' implementation with
Gaussian gridding. Supports 1D/2D/3D data, complex-valued responses,
heteroscedastic variance estimation, and confidence interval computation.
Performance optimized with vectorized 'R' code and compiled helpers via
'Rcpp'/'RcppArmadillo'. Extends the 'FKreg' toolbox of Wang et al. (2022)
<doi:10.48550/arXiv.2204.07716> with 'Python' and 'R' ports. Applied in Li
et al. (2022) <doi:10.1016/j.neuroimage.2022.119190>. Uses 'NUFFT' methods
based on Greengard and Lee (2004) <doi:10.1137/S003614450343200X>,
binning-accelerated kernel estimation of Wand (1994)
<doi:10.1080/10618600.1994.10474656>, and local polynomial regression
framework of Fan and Gijbels (1996, ISBN:978-0412983214).

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
