%global packname  gdalUtilities
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Wrappers for 'GDAL' Utilities Executables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 

%description
R's 'sf' package ships with self-contained 'GDAL' executables, including a
bare bones interface to several 'GDAL'-related utility programs
collectively known as the 'GDAL utilities'. For each of those utilities,
this package provides an R wrapper whose formal arguments closely mirror
those of the 'GDAL' command line interface. The utilities operate on data
stored in files and typically write their output to other files.
Therefore, to process data stored in any of R's more common spatial
formats (i.e. those supported by the 'sp', 'sf', and 'raster' packages),
first write them to disk, then process them with the package's wrapper
functions before reading the outputted results back into R. GDAL function
arguments introduced in GDAL version 3.2.1 or earlier are supported.

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
