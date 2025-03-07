%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  actfts
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Autocorrelation Tools Featured for Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-xts 
Requires:         R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-lifecycle 

%description
The 'actfts' package provides tools for performing autocorrelation
analysis of time series data. It includes functions to compute and
visualize the autocorrelation function (ACF) and the partial
autocorrelation function (PACF). Additionally, it performs the
Dickey-Fuller, KPSS, and Phillips-Perron unit root tests to assess the
stationarity of time series. Theoretical foundations are based on Box and
Cox (1964) <doi:10.1111/j.2517-6161.1964.tb00553.x>, Box and Jenkins
(1976) <isbn:978-0-8162-1234-2>, and Box and Pierce (1970)
<doi:10.1080/01621459.1970.10481180>. Statistical methods are also drawn
from Kolmogorov (1933) <doi:10.1007/BF00993594>, Kwiatkowski et al. (1992)
<doi:10.1016/0304-4076(92)90104-Y>, and Ljung and Box (1978)
<doi:10.1093/biomet/65.2.297>. The package integrates functions from
'forecast' (Hyndman & Khandakar, 2008)
<https://CRAN.R-project.org/package=forecast>, 'tseries' (Trapletti &
Hornik, 2020) <https://CRAN.R-project.org/package=tseries>, 'xts' (Ryan &
Ulrich, 2020) <https://CRAN.R-project.org/package=xts>, and 'stats' (R
Core Team, 2023)
<https://stat.ethz.ch/R-manual/R-devel/library/stats/html/00Index.html>.
Additionally, it provides visualization tools via 'plotly' (Sievert, 2020)
<https://CRAN.R-project.org/package=plotly> and 'reactable' (Glaz, 2023)
<https://CRAN.R-project.org/package=reactable>. The package also
incorporates macroeconomic datasets from the U.S. Bureau of Economic
Analysis: Disposable Personal Income (DPI)
<https://fred.stlouisfed.org/series/DPI>, Gross Domestic Product (GDP)
<https://fred.stlouisfed.org/series/GDP>, and Personal Consumption
Expenditures (PCEC) <https://fred.stlouisfed.org/series/PCEC>.

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
