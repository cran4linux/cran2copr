%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  narfima
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Neural AutoRegressive Fractionally Integrated Moving Average Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-bsts 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-bsts 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Methods and tools for forecasting univariate time series using the NARFIMA
(Neural AutoRegressive Fractionally Integrated Moving Average) model. It
combines neural networks with fractional differencing to capture both
nonlinear patterns and long-term dependencies. The NARFIMA model supports
seasonal adjustment, Box-Cox transformations, optional exogenous
variables, and the computation of prediction intervals. In addition to the
NARFIMA model, this package provides alternative forecasting models
including NARIMA (Neural ARIMA), NBSTS (Neural Bayesian Structural Time
Series), and NNaive (Neural Naive) for performance comparison across
different modeling approaches. The methods are based on algorithms
introduced by Chakraborty et al. (2025) <doi:10.48550/arXiv.2509.06697>.

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
