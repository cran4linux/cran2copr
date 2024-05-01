%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KMLtoSHAPE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Preserving Attribute Values: Converting KML to Shapefile

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sf 

%description
The developed function is designed to facilitate the seamless conversion
of KML (Keyhole Markup Language) files to Shapefiles while preserving
attribute values. It provides a straightforward interface for users to
effortlessly import KML data, extract relevant attributes, and export them
into the widely compatible Shapefile format. The package ensures accurate
representation of spatial data while maintaining the integrity of
associated attribute information. For details see, Flores, G. (2021).
<DOI:10.1007/978-3-030-63665-4_15>. Whether for spatial analysis,
visualization, or data interoperability, it simplifies the conversion
process and empowers users to seamlessly work with geospatial datasets.

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
