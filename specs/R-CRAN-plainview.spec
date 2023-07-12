%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plainview
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Plot Raster Images Interactively on a Plain HTML Canvas

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-methods 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-png 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-viridisLite 

%description
Provides methods for plotting potentially large (raster) images
interactively on a plain HTML canvas. In contrast to package 'mapview'
data are plotted without background map, but data can be projected to any
spatial coordinate reference system. Supports plotting of classes
'RasterLayer', 'RasterStack', 'RasterBrick' (from package 'raster') as
well as 'png' files located on disk. Interactivity includes zooming,
panning, and mouse location information. In case of multi-layer
'RasterStacks' or 'RasterBricks', RGB image plots are created (similar to
'raster::plotRGB' - but interactive).

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
