%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtfs2gps
%global packver   3.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Converting Transport Data from GTFS Format to GPS-Like Records

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-gtfstools >= 2.0.1
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cpp11 >= 0.4.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-gtfstools >= 2.0.1
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-units 

%description
Convert general transit feed specification (GTFS) data to global
positioning system (GPS) records in 'data.table' format. It also has
functions to post-process these GPS records, for example converting them
to simple feature format.

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
