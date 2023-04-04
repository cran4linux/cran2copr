%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgbif
%global packver   3.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the Global Biodiversity Information Facility API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-crul >= 0.7
BuildRequires:    R-CRAN-oai >= 0.2.2
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wk 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-crul >= 0.7
Requires:         R-CRAN-oai >= 0.2.2
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-CRAN-wk 

%description
A programmatic interface to the Web Service methods provided by the Global
Biodiversity Information Facility (GBIF;
<https://www.gbif.org/developer/summary>). GBIF is a database of species
occurrence records from sources all over the globe. rgbif includes
functions for searching for taxonomic names, retrieving information on
data providers, getting species occurrence records, getting counts of
occurrence records, and using the GBIF tile map service to make rasters
summarizing huge amounts of data.

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
