%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stars
%global packver   0.6-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Spatiotemporal Arrays, Raster and Vector Data Cubes

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.15
BuildRequires:    R-CRAN-classInt >= 0.4.1
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf >= 1.0.15
Requires:         R-CRAN-classInt >= 0.4.1
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-units 

%description
Reading, manipulating, writing and plotting spatiotemporal arrays (raster
and vector data cubes) in 'R', using 'GDAL' bindings provided by 'sf', and
'NetCDF' bindings by 'ncmeta' and 'RNetCDF'.

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
