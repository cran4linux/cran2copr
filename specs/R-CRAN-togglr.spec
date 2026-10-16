%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  togglr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for the 'Toggl Track' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-filelock >= 1.0.2
BuildRequires:    R-CRAN-cachem >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-filelock >= 1.0.2
Requires:         R-CRAN-cachem >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-utils 

%description
Read and write time entries, projects and clients of the 'Toggl Track'
time tracker <https://toggl.com> from R, and download its reports. Reads
never return silently truncated or empty results: HTTP errors are raised,
the hourly quota and rate limits are respected, and paginated reports are
checked for completeness.

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
