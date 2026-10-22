%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsexplorer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory and Diagnostic Tools for Time Series and Forecasts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Exploratory, descriptive and diagnostic tools for univariate and
multivariate time series and tools to evaluate and compare forecasts:
summary statistics and gaussianity tests; sample autocorrelation functions
with the Ljung and Box (1978) <doi:10.1093/biomet/65.2.297> and Monti
(1994) <doi:10.2307/2337080> tests; information criteria and Granger
(1969) <doi:10.2307/1912791> causality; unit root tests of Dickey and
Fuller (1979) <doi:10.1080/01621459.1979.10482531> and Phillips and Perron
(1988) <doi:10.1093/biomet/75.2.335>; the cointegration test of Johansen
(1988) <doi:10.1016/0165-1889(88)90041-3>; heteroskedasticity tests;
non-linearity tests of McLeod and Li (1983)
<doi:10.1111/j.1467-9892.1983.tb00373.x>, Tsay (1986)
<doi:10.1093/biomet/73.2.461> and Brock, Dechert, Scheinkman and LeBaron
(1996) <doi:10.1080/07474939608800353>; spectral analysis; and forecast
accuracy measures with the Diebold and Mariano (1995)
<doi:10.1080/07350015.1995.10524599>, sign and Wilcoxon tests. Every tool
is a pure function returning an object with print and plot methods; the
graphical interfaces tooltest() and toolforecast() ('Tcl/Tk' windows or
'shiny' applications) give interactive access to all of them.

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
