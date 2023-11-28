%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seasonalityPlot
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Seasonality Variation Plots of Stock Prices and Cryptocurrencies

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-htmltools 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 

%description
The price action at any given time is determined by investor sentiment and
market conditions. Although there is no established principle, over a long
period of time, things often move with a certain periodicity. This is
sometimes referred to as anomaly. The seasonPlot() function in this
package calculates and visualizes the average value of price movements
over a year for any given period. In addition, the monthly increase or
decrease in price movement is represented with a colored background. This
seasonPlot() function can use the same symbols as the 'quantmod' package
(e.g. ^IXIC, ^DJI, SPY, BTC-USD, and ETH-USD etc).

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
