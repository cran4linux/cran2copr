%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OpenMindat
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quickly Retrieve Datasets from the 'mindat.org' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.8.4
BuildRequires:    R-CRAN-httr >= 1.4.4
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-jsonlite >= 1.8.4
Requires:         R-CRAN-httr >= 1.4.4
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-usethis 

%description
'Mindat' ('mindat.org') is one of the world's most widely used databases
of mineral species and their distribution. Many scientists in mineralogy,
geochemistry, petrology, and other Earth and planetary disciplines have
been using the 'Mindat' data. Still, an open data service and the machine
interface have never been fully established. To meet the overwhelming data
needs, the 'Mindat' team has built an API
(<https://api.mindat.org/schema/redoc/>) for data access.'OpenMindat' R
package provides valuable functions to bridge the data highway, connecting
users' data requirements to the 'Mindat' API server and assist with
retrieval and initial processing to improve efficiency further and lower
the barrier of data query and access to scientists. 'OpenMindat' provides
friendly and extensible data retrieval functions, including the subjects
of geomaterials (e.g., rocks, minerals, synonyms, variety, mixture, and
commodity), localities, and the IMA (International Mineralogical
Association)-approved mineral list. 'OpenMindat' R package will accelerate
the process of data-intensive studies in mineral informatics and lead to
more scientific discoveries.

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
