%global __brp_check_rpaths %{nil}
%global packname  GNRS
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access the 'Geographic Name Resolution Service'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 

%description
Provides tools for interacting with the 'geographic name resolution
service' ('GNRS') API <https://github.com/ojalaquellueva/gnrs> and
associated functionality. The 'GNRS' is a batch application for resolving
& standardizing political division names against standard name in the
geonames database <http://www.geonames.org/>. The 'GNRS' resolves
political division names at three levels: country, state/province and
county/parish. Resolution is performed in a series of steps, beginning
with direct matching to standard names, followed by direct matching to
alternate names in different languages, followed by direct matching to
standard codes (such as ISO and FIPS codes). If direct matching fails, the
'GNRS' attempts to match to standard and then alternate names using fuzzy
matching, but does not perform fuzzing matching of political division
codes. The 'GNRS' works down the political division hierarchy, stopping at
the current level if all matches fail. In other words, if a country cannot
be matched, the 'GNRS' does not attempt to match state or county.

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
