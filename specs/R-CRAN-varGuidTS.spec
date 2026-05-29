%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  varGuidTS
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Variance-Guided Time-Series Modeling for Temporal Risk Detection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 

%description
Fits balanced-panel autoregressive models with conditional
heteroscedasticity for temporal risk detection. The main estimator
combines autoregressive exogenous mean modeling with GARCH-X variance
modeling, subject-specific baseline terms, shared population coefficients,
and L1 penalization for high-dimensional covariates. The package returns
conditional mean and variance estimates, coefficient summaries,
simulations, and exceedance-based risk scores defined as estimated
conditional threshold-exceedance probabilities. The implementation builds
on the lasso of Tibshirani (1996)
<doi:10.1111/j.2517-6161.1996.tb02080.x>, generalized autoregressive
conditional heteroscedasticity of Bollerslev (1986)
<doi:10.1016/0304-4076(86)90063-1>, and L1-regularized high-dimensional
time-series modeling of Medeiros and Mendes (2016)
<doi:10.1016/j.jeconom.2015.10.011>.

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
