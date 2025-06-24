%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slopes
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Slopes of Roads, Rivers and Trajectories

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-colorspace 

%description
Calculates the slope (longitudinal gradient or steepness) of linear
geographic features such as roads (for more details, see Ariza-López et
al. (2019) <doi:10.1038/s41597-019-0147-x>) and rivers (for more details,
see Cohen et al. (2018) <doi:10.1016/j.jhydrol.2018.06.066>). It can use
local Digital Elevation Model (DEM) data or download DEM data via the
'ceramic' package. The package also provides functions to add elevation
data to linestrings and visualize elevation profiles.

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
