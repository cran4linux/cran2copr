%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ichimoku
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization and Tools for Ichimoku Kinko Hyo Strategies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-mirai >= 0.12.0
BuildRequires:    R-CRAN-nanonext >= 0.12.0
BuildRequires:    R-CRAN-RcppSimdJson >= 0.1.9
BuildRequires:    R-CRAN-secretbase 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-mirai >= 0.12.0
Requires:         R-CRAN-nanonext >= 0.12.0
Requires:         R-CRAN-RcppSimdJson >= 0.1.9
Requires:         R-CRAN-secretbase 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
An implementation of 'Ichimoku Kinko Hyo', also commonly known as 'cloud
charts'. Static and interactive visualizations with tools for creating,
backtesting and development of quantitative 'ichimoku' strategies. As
described in Sasaki (1996, ISBN:4925152009), the technique is a refinement
on candlestick charting, originating from Japan and now in widespread use
in technical analysis worldwide. Translating as 'one-glance equilibrium
chart', it allows the price action and market structure of financial
securities to be determined 'at-a-glance'. Incorporates an interface with
the OANDA fxTrade API <https://developer.oanda.com/> for retrieving
historical and live streaming price data for major currencies, metals,
commodities, government bonds and stock indices.

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
