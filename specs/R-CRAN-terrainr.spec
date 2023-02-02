%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  terrainr
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Landscape Visualizations in R and 'Unity'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-magick >= 2.5.0
BuildRequires:    R-CRAN-sf >= 1.0.5
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-unifir 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-magick >= 2.5.0
Requires:         R-CRAN-sf >= 1.0.5
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-unifir 
Requires:         R-CRAN-units 

%description
Functions for the retrieval, manipulation, and visualization of
'geospatial' data, with an aim towards producing '3D' landscape
visualizations in the 'Unity' '3D' rendering engine. Functions are also
provided for retrieving elevation data and base map tiles from the 'USGS'
National Map <https://apps.nationalmap.gov/services/>.

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
