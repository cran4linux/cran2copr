%global __brp_check_rpaths %{nil}
%global packname  sara4r
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          An R-GUI for Spatial Analysis of Surface Runoff using the NRCS-CN Method

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 

%description
A Graphical user interface to calculate the rainfall-runoff relation using
the Natural Resources Conservation Service - Curve Number method (NRCS-CN
method) but include modifications by Hawkins et al., (2002) about the
Initial Abstraction. This GUI follows the programming logic of a
previously published software (Hernandez-Guzman et al.,
2011)<doi:10.1016/j.envsoft.2011.07.006>. It is a raster-based GIS tool
that outputs runoff estimates from Land use/land cover and hydrologic soil
group maps. This package has already been published in Journal of
Hydroinformatics (Hernandez-Guzman et al.,
2021)<doi:10.2166/hydro.2020.087> but it is under constant development at
the Institute about Natural Resources Research (INIRENA) from the
Universidad Michoacana de San Nicolas de Hidalgo and represents a
collaborative effort between the Hydro-Geomatic Lab (INIRENA) with the
Environmental Management Lab (CIAD, A.C.).

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
