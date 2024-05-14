%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DatastreamR
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Datastream API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-ini 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-ini 
Requires:         R-CRAN-stringr 
Requires:         R-methods 

%description
Access Datastream content through
<https://product.datastream.com/dswsclient/Docs/Default.aspx>., our
historical financial database with over 35 million individual instruments
or indicators across all major asset classes, including over 19 million
active economic indicators. It features 120 years of data, across 175
countries – the information you need to interpret market trends, economic
cycles, and the impact of world events.  Data spans bond indices, bonds,
commodities, convertibles, credit default swaps, derivatives, economics,
energy, equities, equity indices, ESG, estimates, exchange rates, fixed
income, funds, fundamentals, interest rates, and investment trusts. Unique
content includes I/B/E/S Estimates, Worldscope Fundamentals, point-in-time
data, and Reuters Polls.  Alongside the content, sit a set of powerful
analytical tools for exploring relationships between different asset
types, with a library of customizable analytical functions.  In-house
timeseries can also be uploaded using the package to comingle with
Datastream maintained datasets, use with these analytical tools and
displayed in Datastream’s flexible charting facilities in Microsoft
Office.

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
