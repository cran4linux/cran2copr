%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtfs2gps
%global packver   2.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Converting Transport Data from GTFS Format to GPS-Like Records

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-gtfstools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-gtfstools 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-units 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-checkmate 

%description
Convert general transit feed specification (GTFS) data to global
positioning system (GPS) records in 'data.table' format. It also has some
functions to subset GTFS data in time and space and to convert both
representations to simple feature format.

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
