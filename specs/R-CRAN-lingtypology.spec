%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lingtypology
%global packver   1.1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.20
Release:          1%{?dist}%{?buildtag}
Summary:          Linguistic Typology and Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.minicharts 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.minicharts 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringdist 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 

%description
Provides R with the Glottolog database <https://glottolog.org/> and some
more abilities for purposes of linguistic mapping. The Glottolog database
contains the catalogue of languages of the world. This package helps
researchers to make a linguistic maps, using philosophy of the
Cross-Linguistic Linked Data project <https://clld.org/>, which allows for
while at the same time facilitating uniform access to the data across
publications. A tutorial for this package is available on GitHub pages
<https://docs.ropensci.org/lingtypology/> and package vignette. Maps
created by this package can be used both for the investigation and
linguistic teaching. In addition, package provides an ability to download
data from typological databases such as WALS, AUTOTYP and some others and
to create your own database website.

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
