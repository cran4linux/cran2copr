%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtfsrouter
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Routing with 'GTFS' (General Transit Feed Specification) Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-geodist 
Requires:         R-methods 

%description
Use 'GTFS' (General Transit Feed Specification) data for routing from
nominated start and end stations, for extracting 'isochrones', and travel
times from any nominated start station to all other stations.

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
