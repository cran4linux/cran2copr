%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cyclestreets
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cycle Routing and Data for Cycling Advocacy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 

%description
An interface to the cycle routing/data services provided by
'CycleStreets', a not-for-profit social enterprise and advocacy
organisation.  The application programming interfaces (APIs) provided by
'CycleStreets' are documented at (<https://www.cyclestreets.net/api/>).
The focus of this package is the journey planning API, which aims to
emulate the routes taken by a knowledgeable cyclist.  An innovative
feature of the routing service of its provision of fastest, quietest and
balanced profiles.  These represent routes taken to minimise time, avoid
traffic and compromise between the two, respectively.

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
