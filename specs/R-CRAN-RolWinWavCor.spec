%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RolWinWavCor
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Rolling Window Wavelet Correlation Between Two Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim 
Requires:         R-CRAN-waveslim 

%description
Estimates and plots as a heat map the rolling window wavelet correlation
(RWWC) coefficients statistically significant (within the 95%% CI) between
two regular (evenly spaced) time series. 'RolWinWavCor' also plots at the
same graphic the time series under study. The 'RolWinWavCor' was designed
for financial time series, but this software can be used with other kinds
of data (e.g., climatic, ecological, geological, etc). The functions
contained in 'RolWinWavCor' are highly flexible since these contains some
parameters to personalize the time series under analysis and the heat maps
of the rolling window wavelet correlation coefficients. Moreover, we have
also included a data set (named EU_stock_markets) that contains nine
European stock market indices to exemplify the use of the functions
contained in 'RolWinWavCor'. Methods derived from Polanco-Martínez et al
(2018) <doi:10.1016/j.physa.2017.08.065>).

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
