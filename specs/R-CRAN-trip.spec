%global packname  trip
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the Analysis of Animal Track Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reproj 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-traipse 
BuildRequires:    R-CRAN-crsmeta 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reproj 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-traipse 
Requires:         R-CRAN-crsmeta 

%description
Functions for accessing and manipulating spatial data for animal tracking,
with straightforward coercion from and to other formats. Filter for speed
and create time spent maps from animal track data. There are coercion
methods to convert between 'trip' and 'ltraj' from 'adehabitatLT', and
between 'trip' and 'psp' and 'ppp' from 'spatstat'. Trip objects can be
created from raw or grouped data frames, and from types in the 'sp', 'sf',
'amt', 'trackeR', 'mousetrap', and other packages.

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
