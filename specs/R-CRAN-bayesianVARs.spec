%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesianVARs
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          MCMC Estimation of Bayesian Vectorautoregressions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-stochvol >= 3.0.3
BuildRequires:    R-CRAN-factorstochvol >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-GIGrvg >= 0.7
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-stochvol >= 3.0.3
Requires:         R-CRAN-factorstochvol >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-GIGrvg >= 0.7
Requires:         R-CRAN-colorspace 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Efficient Markov Chain Monte Carlo (MCMC) algorithms for the fully
Bayesian estimation of vectorautoregressions (VARs) featuring stochastic
volatility (SV). Implements state-of-the-art shrinkage priors following
Gruber & Kastner (2025) <doi:10.1016/j.ijforecast.2025.02.001>. Efficient
equation-per-equation estimation following Kastner & Huber (2020)
<doi:10.1002/for.2680> and Carrerio et al. (2021)
<doi:10.1016/j.jeconom.2021.11.010>.

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
