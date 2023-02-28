%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  egcm
%global packver   1.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Engle-Granger Cointegration Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-urca 
Requires:         R-parallel 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-quantmod 
Requires:         R-methods 

%description
An easy-to-use implementation of the Engle-Granger two-step procedure for
identifying pairs of cointegrated series.  It is geared towards the
analysis of pairs of securities.  Summary and plot functions are provided,
and the package is able to fetch closing prices of securities from Yahoo.
A variety of unit root tests are supported, and an improved unit root test
is included.

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
