%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggalt
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Coordinate Systems, 'Geoms', Statistical Transformations, Scales and Fonts for 'ggplot2'

License:          AGPL + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 3.4.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-proj4 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-plotly >= 3.4.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-proj4 
Requires:         R-CRAN-scales 
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-tibble 

%description
A compendium of new geometries, coordinate systems, statistical
transformations, scales and fonts for 'ggplot2', including splines, 1d and
2d densities, univariate average shifted histograms, a new map coordinate
system based on the 'PROJ.4'-library along with geom_cartogram() that
mimics the original functionality of geom_map(), formatters for "bytes", a
stat_stepribbon() function, increased 'plotly' compatibility and the
'StateFace' open source font 'ProPublica'. Further new functionality
includes lollipop charts, dumbbell charts, the ability to encircle points
and coordinate-system-based text annotations.

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
