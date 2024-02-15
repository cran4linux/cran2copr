%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdm
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Metrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Formula 
Requires:         R-methods 

%description
Implementation of selected high-dimensional statistical and econometric
methods for estimation and inference. Efficient estimators and uniformly
valid confidence intervals for various low-dimensional causal/ structural
parameters are provided which appear in high-dimensional approximately
sparse models. Including functions for fitting heteroscedastic robust
Lasso regressions with non-Gaussian errors and for instrumental variable
(IV) and treatment effect estimation in a high-dimensional setting.
Moreover, the methods enable valid post-selection inference and rely on a
theoretically grounded, data-driven choice of the penalty. Chernozhukov,
Hansen, Spindler (2016) <arXiv:1603.01700>.

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
