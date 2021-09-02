%global __brp_check_rpaths %{nil}
%global packname  mapSpain
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Administrative Boundaries of Spain

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 3.0
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-countrycode >= 1.2.0
BuildRequires:    R-CRAN-sf >= 0.9
BuildRequires:    R-CRAN-slippymath >= 0.3.1
BuildRequires:    R-CRAN-rappdirs >= 0.3.0
BuildRequires:    R-CRAN-giscoR >= 0.2.4
BuildRequires:    R-CRAN-png >= 0.1.5
BuildRequires:    R-utils 
Requires:         R-CRAN-raster >= 3.0
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-countrycode >= 1.2.0
Requires:         R-CRAN-sf >= 0.9
Requires:         R-CRAN-slippymath >= 0.3.1
Requires:         R-CRAN-rappdirs >= 0.3.0
Requires:         R-CRAN-giscoR >= 0.2.4
Requires:         R-CRAN-png >= 0.1.5
Requires:         R-utils 

%description
Administrative Boundaries of Spain at several levels (CCAA, Provinces,
Municipalities) based on the GISCO Eurostat database
<https://ec.europa.eu/eurostat/web/gisco> and 'CartoBase SIANE' from
'Instituto Geografico Nacional' <https://www.ign.es/>.  It also provides a
'leaflet' plugin and the ability of downloading and processing static
tiles.

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
