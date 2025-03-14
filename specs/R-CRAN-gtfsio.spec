%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtfsio
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write General Transit Feed Specification (GTFS) Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fs 
Requires:         R-utils 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-jsonlite 

%description
Tools for the development of packages related to General Transit Feed
Specification (GTFS) files. Establishes a standard for representing GTFS
feeds using R data types. Provides fast and flexible functions to read and
write GTFS feeds while sticking to this standard. Defines a basic 'gtfs'
class which is meant to be extended by packages that depend on it. And
offers utility functions that support checking the structure of GTFS
objects.

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
