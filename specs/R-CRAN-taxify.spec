%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  taxify
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Offline Taxonomic Name Matching Against Darwin Core Backbones

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vectra >= 0.14.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-vectra >= 0.14.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 

%description
Matches taxonomic names against local copies of published backbones
('Catalogue of Life', 'GBIF Backbone Taxonomy', 'ITIS', 'World Flora
Online', 'WoRMS', 'NCBI Taxonomy', 'Open Tree of Life', 'Euro+Med',
'Species Fungorum', 'AlgaeBase', 'FishBase', 'SeaLifeBase', 'Reptile
Database', 'LCVP', 'WCVP', 'Mammal Diversity Database', 'AviList', 'LPSN')
and two vegetation classifications, and resolves each name to its accepted
name. It performs the name-resolution step of 'taxize' and 'WorldFlora',
run offline against these files. Names are cleaned of authors and
qualifiers, matched exactly and then by edit distance within their genus,
and followed from synonym to accepted name, with the backbone version
recorded on every row. Published trait, status and distribution datasets
are joined on the accepted name, and so is a table the user supplies.
Matching runs in the 'vectra' column-store engine.

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
