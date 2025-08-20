%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsp
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Shrinkage Process and Change Point Detection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-pgdraw 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppZiggurat 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stochvol 
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-fda 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MCMCpack 
Requires:         R-methods 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-pgdraw 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppZiggurat 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-CRAN-stochvol 
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-glue 

%description
Provides efficient Markov chain Monte Carlo (MCMC) algorithms for dynamic
shrinkage processes, which extend global-local shrinkage priors to the
time series setting by allowing shrinkage to depend on its own past. These
priors yield locally adaptive estimates, useful for time series and
regression functions with irregular features. The package includes full
MCMC implementations for trend filtering using dynamic shrinkage on signal
differences, producing locally constant or linear fits with adaptive
credible bands. Also included are models with static shrinkage and
normal-inverse-Gamma priors for comparison. Additional tools cover dynamic
regression with time-varying coefficients and B-spline models with
shrinkage on basis differences, allowing for flexible curve-fitting with
unequally spaced data. Some support for heteroscedastic errors, outlier
detection, and change point estimation. Methods in this package are
described in Kowal et al. (2019) <doi:10.1111/rssb.12325>, Wu et al.
(2024) <doi:10.1080/07350015.2024.2362269>, Schafer and Matteson (2024)
<doi:10.1080/00401706.2024.2407316>, and Cho and Matteson (2024)
<doi:10.48550/arXiv.2408.11315>.

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
