%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wqrr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet Quantile Regression Toolbox

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.0
BuildRequires:    R-CRAN-plotly >= 4.0.0
BuildRequires:    R-CRAN-waveslim >= 1.8
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-quantreg >= 5.0
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-CRAN-waveslim >= 1.8
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
A comprehensive toolbox for wavelet-domain quantile analyses of bivariate
and multivariate time series. Provides Wavelet Quantile Regression and
Multivariate Wavelet Quantile Regression after Adebayo and Ozkan (2024)
<doi:10.1016/j.jclepro.2024.140832>, Wavelet Quantile-on-Quantile
regression with bootstrap p-values extending Sim and Zhou (2015)
<doi:10.1016/j.jbankfin.2015.01.013>, the nonparametric
Causality-in-Quantiles test of Balcilar, Gupta and Pierdzioch (2016)
<doi:10.1016/j.resourpol.2016.04.004> together with its wavelet variant,
Wavelet Quantile Mediation and Moderation, Wavelet Quantile Correlation,
and a wavelet-based nonparametric Quantile Density estimator. The Maximal
Overlap Discrete Wavelet Transform (MODWT) decomposition is performed via
'waveslim' and Short / Medium / Long band aggregation is supported
throughout. For plain Quantile-on-Quantile regression see the companion
CRAN package 'QuantileOnQuantile'. All interactive 3D surfaces, heatmaps
and contour plots default to the 'MATLAB' 'Parula' colour map.

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
