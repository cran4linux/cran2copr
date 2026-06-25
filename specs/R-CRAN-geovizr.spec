%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geovizr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Cartography

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sf 

%description
Create a wide range of interactive, zoomable vector maps. This package is
an 'R' binding for the 'geoviz' 'JavaScript' library
<https://github.com/riatelab/geoviz/>, itself based on the 'd3.js'
ecosystem <doi:10.1109/TVCG.2011.185>. Like the original 'JavaScript'
library, the package takes advantage of the many features provided by
'd3.js': proportional symbols, pictograms, typologies, choropleth maps,
spikes, tiles, Dorling cartograms, and more. It can also be used to create
pretty static vectorial maps in 'svg' format, suitable for editorial
cartography.

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
