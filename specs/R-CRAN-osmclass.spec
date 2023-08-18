%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  osmclass
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Classify Open Street Map Features

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-collapse >= 1.9.6
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-collapse >= 1.9.6
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringi 

%description
Classify Open Street Map (OSM) features into meaningful functional or
analytical categories. Designed for OSM PBF files, e.g. from
<https://download.geofabrik.de/> imported as spatial data frames. A
classification consists of a list of categories that are related to
certain OSM tags and values. Given a layer from an OSM PBF file and a
classification, the main osm_classify() function returns a classification
data table giving, for each feature, the primary and alternative
categories (if there is overlap) assigned, and the tag(s) and value(s)
matched on. The package also contains a classification of OSM features by
economic function/significance, following Krantz (2023)
<https://www.ssrn.com/abstract=4537867>.

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
