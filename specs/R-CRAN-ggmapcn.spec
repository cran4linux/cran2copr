%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggmapcn
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Customizable China and Global Map Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-terra >= 1.7
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-tidyterra >= 0.6.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-grid 
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-terra >= 1.7
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-tidyterra >= 0.6.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-digest 
Requires:         R-grid 

%description
Provides 'ggplot2' layers and annotations for thematic mapping of China
and the world. Uses administrative division data from the 'Tianditu'
geospatial information service and separate layers for land borders,
coastlines, and maritime boundaries. Supports province-, city-, and
county-level maps, map projections, graticules, scale bars, north arrows,
boundary buffers, and elevation and vegetation raster layers. The package
provides default map datasets. Larger data files are hosted in a companion
repository <https://github.com/Rimagination/ggmapcn-data> and retrieved as
needed.

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
