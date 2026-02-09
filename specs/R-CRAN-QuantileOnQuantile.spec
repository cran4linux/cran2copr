%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuantileOnQuantile
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile-on-Quantile Regression Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.0
BuildRequires:    R-CRAN-plotly >= 4.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-quantreg >= 5.0
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-stats 
Requires:         R-utils 

%description
Implements the Quantile-on-Quantile (QQ) regression methodology developed
by Sim and Zhou (2015) <doi:10.1016/j.jbankfin.2015.01.013>. QQ regression
estimates the effect that quantiles of one variable have on quantiles of
another, capturing the dependence between distributions. The package
provides functions for QQ regression estimation, 3D surface visualization
with 'MATLAB'-style color schemes ('Jet', 'Viridis', 'Plasma'), heatmaps,
contour plots, and quantile correlation analysis. Uses 'quantreg' for
quantile regression and 'plotly' for interactive visualizations.
Particularly useful for examining relationships between financial
variables, oil prices, and stock returns under different market
conditions.

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
