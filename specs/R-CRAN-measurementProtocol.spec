%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  measurementProtocol
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Send Data from R to the Measurement Protocol

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-rappdirs >= 0.3.3
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-rappdirs >= 0.3.3
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-utils 

%description
Send server-side tracking data from R. The Measurement Protocol version 2
<https://developers.google.com/analytics/devguides/collection/protocol/ga4>
allows sending HTTP tracking events from R code.

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
