%global __brp_check_rpaths %{nil}
%global packname  ichimoku
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization and Tools for Ichimoku Kinko Hyo Strategies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
An implementation of 'Ichimoku Kinko Hyo', also commonly known as 'cloud
charts'. Static and interactive visualizations with tools for creating,
backtesting and development of quantitative 'ichimoku' strategies. As
described in Sasaki (1996, ISBN:4925152009), the technique is a refinement
on candlestick charting originating from Japan, now in widespread use in
technical analysis worldwide. Translating as 'one-glance equilibrium
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
