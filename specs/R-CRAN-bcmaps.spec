%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bcmaps
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Map Layers and Spatial Utilities for British Columbia

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-bcdata >= 0.5.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-bcdata >= 0.5.0
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-methods 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Various layers of B.C., including administrative boundaries, natural
resource management boundaries, census boundaries etc. All layers are
available in BC Albers (<https://spatialreference.org/ref/epsg/3005/>)
equal-area projection, which is the B.C. government standard. The layers
are sourced from the British Columbia and Canadian government under open
licenses, including B.C. Data Catalogue (<https://data.gov.bc.ca>), the
Government of Canada Open Data Portal
(<https://open.canada.ca/en/using-open-data>), and Statistics Canada
(<https://www.statcan.gc.ca/en/reference/licence>).

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
