%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mongolmaps
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maps and Administrative Boundaries of Mongolia and Ulaanbaatar

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.12
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.12
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-curl 
Requires:         R-grDevices 
Requires:         R-CRAN-openssl 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
Ready-to-use 'sf' maps of Mongolia at every openly available
administrative level: country, economic regions, aimags (provinces), soums
and Ulaanbaatar districts, and Ulaanbaatar khoroos (subdistricts), with
codes and names for every bag. Provides a crosswalk between English and
Cyrillic names, common spelling variants, ISO 3166-2 codes, humanitarian
P-codes and National Statistics Office codes; helpers to join statistics
to maps; thematic layers (settlements, rivers, lakes, roads, railways,
airports, elevation, land cover, population and protected areas); and
quick 'ggplot2' and 'leaflet' maps. Boundaries derive from the Common
Operational Dataset published by the National Statistics Office of
Mongolia and the United Nations Office for the Coordination of
Humanitarian Affairs <https://data.humdata.org/dataset/cod-ab-mng>.

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
