%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cryptoQuotes
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Open Access to Cryptocurrency Market Data, Sentiment Indicators and Interactive Charts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.2.1
BuildRequires:    R-CRAN-plotly >= 4.10.4
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-zoo >= 1.8.12
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-TTR >= 0.24.4
BuildRequires:    R-CRAN-xts >= 0.14.0
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 5.2.1
Requires:         R-CRAN-plotly >= 4.10.4
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-zoo >= 1.8.12
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-TTR >= 0.24.4
Requires:         R-CRAN-xts >= 0.14.0
Requires:         R-utils 

%description
This high-level API client provides open access to cryptocurrency market
data, sentiment indicators, and interactive charting tools. The data is
sourced from major cryptocurrency exchanges via 'curl' and returned in
'xts'-format. The data comes in open, high, low, and close (OHLC) format
with flexible granularity, ranging from seconds to months. This
flexibility makes it ideal for developing and backtesting trading
strategies or conducting detailed market analysis.

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
