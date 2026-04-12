%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fred
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access 'Federal Reserve Economic Data'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-tools 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-tools 

%description
Provides clean, tidy access to economic data from the 'Federal Reserve
Economic Data' ('FRED') API <https://fred.stlouisfed.org/docs/api/fred/>.
'FRED' is maintained by the 'Federal Reserve Bank of St. Louis' and
contains over 800,000 time series from 118 sources covering GDP,
employment, inflation, interest rates, trade, and more. Dedicated
functions fetch series observations, search for series, browse categories,
releases, and tags, and retrieve series metadata. Multiple series can be
fetched in a single call, in long or wide format. Server-side unit
transformations (percent change, log, etc.) and frequency aggregation are
supported, with readable transform aliases such as 'yoy_pct' and
'log_diff'. Real-time and vintage helpers (built on 'ALFRED') return a
series as it appeared on a given date, the first-release version, every
revision, or a panel of selected vintages. Data is cached locally for
subsequent calls. This product uses the 'FRED' API but is not endorsed or
certified by the 'Federal Reserve Bank of St. Louis'.

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
