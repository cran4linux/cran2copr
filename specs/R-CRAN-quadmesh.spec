%global __brp_check_rpaths %{nil}
%global packname  quadmesh
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quadrangle Mesh

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-reproj >= 0.4.0
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-palr 
Requires:         R-CRAN-reproj >= 0.4.0
Requires:         R-CRAN-raster 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-png 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-palr 

%description
Create surface forms from matrix or 'raster' data for flexible plotting
and conversion to other mesh types. The functions 'quadmesh' or
'triangmesh' produce a continuous surface as a 'mesh3d' object as used by
the 'rgl' package. This is used for plotting raster data in 3D (optionally
with texture), and allows the application of a map projection without data
loss and many processing applications that are restricted by inflexible
regular grid rasters. There are discrete forms of these continuous
surfaces available with 'dquadmesh' and 'dtriangmesh' functions.

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
