%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixqr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extensible Finite Mixtures of Quantile and Expectile Regressions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-quantreg 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
An extensible expectation-maximization (EM) framework for finite mixtures
of quantile regressions (clusterwise / mixture-of-experts quantile
regression). A single EM substrate with an engine/extension contract
carries a family of capabilities: the core free-weight mixture of Wu and
Yao (2016) <doi:10.1016/j.csda.2014.04.014> -- a fast asymmetric-Laplace
path and the nonparametric kernel-density EM with components constrained
to have their tau-quantile equal to zero (Hall and Presnell 1999 device);
expectile and M-quantile component-loss families (Newey and Powell 1987;
Breckling and Chambers 1988); component-specific penalized variable
selection (SCAD / adaptive-LASSO, the quantile analogue of Khalili and
Chen 2007); and joint multi-quantile estimation with a shared latent
classification and non-crossing component curves. Provides
classification-aware standard errors (sparsity and stochastic-EM multiple
imputation), multi-start estimation, component-count selection, and
prediction. The companion package 'mixqrgate' adds location-varying
gating.

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
