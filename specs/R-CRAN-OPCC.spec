%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OPCC
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Open Postal Code Correspondence

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 

%description
An open, fully reproducible alternative to closed postal code conversion
files, giving source-qualified many-to-many correspondence between Ontario
postal codes and Statistics Canada 2021 census geographies. Every
published artifact can be rebuilt step by step from public sources using
the included build functions, so any user can reproduce and audit the
conversion end to end. Lookup results retain allocation weights, evidence
source, lineage, method, and vintage; unmatched postal codes remain
explicit, and versioned release artifacts are checksum-verified before
use. A built-in 'shiny' application provides a point-and-click interface
for joining, mapping, and exporting results. Correspondences are derived
from the Statistics Canada National Address Register
<https://www150.statcan.gc.ca/n1/pub/46-26-0002/462600022022001-eng.htm>,
the 2021 Census Geographic Attribute File
<https://www12.statcan.gc.ca/census-recensement/2021/geo/aip-pia/attribute-attribs/index-eng.cfm>,
and the GeoNames postal code export
<https://download.geonames.org/export/zip/>. The package does not
redistribute Canada Post, PCCF, or PCCF+ data and does not claim
authoritative postal assignments.

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
