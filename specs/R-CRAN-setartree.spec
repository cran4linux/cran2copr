%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  setartree
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          SETAR-Tree - A Novel and Accurate Tree Algorithm for Global Time Series Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-parallel 

%description
The implementation of a forecasting-specific tree-based model that is in
particular suitable for global time series forecasting, as proposed in
Godahewa et al. (2022) <arXiv:2211.08661v1>. The model uses the concept of
Self Exciting Threshold Autoregressive (SETAR) models to define the node
splits and thus, the model is named SETAR-Tree. The SETAR-Tree uses some
time-series-specific splitting and stopping procedures. It trains global
pooled regression models in the leaves allowing the models to learn
cross-series information. The depth of the tree is controlled by
conducting a statistical linearity test as well as measuring the error
reduction percentage at each node split. Thus, the SETAR-Tree requires
minimal external hyperparameter tuning and provides competitive results
under its default configuration. A forest is developed by extending the
SETAR-Tree. The SETAR-Forest combines the forecasts provided by a
collection of diverse SETAR-Trees during the forecasting process.

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
