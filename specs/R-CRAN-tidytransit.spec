%global __brp_check_rpaths %{nil}
%global packname  tidytransit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read, Validate, Analyze, and Map Files in the General Transit Feed Specification

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 2.0.1
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-gtfsio >= 0.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-zip >= 2.0.1
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-gtfsio >= 0.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-checkmate 

%description
Read General Transit Feed Specification (GTFS) zipfiles into a list of R
dataframes. Perform validation of the data structure against the
specification. Analyze the headways and frequencies at routes and stops.
Create maps and perform spatial analysis on the routes and stops. Please
see the GTFS documentation here for more detail: <http://gtfs.org/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
