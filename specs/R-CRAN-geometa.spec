%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geometa
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Reading and Writing ISO/OGC Geographic Metadata

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-crayon 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-crayon 

%description
Provides facilities to read, write and validate geographic metadata
defined with ISO TC211 / OGC ISO geographic information metadata
standards, and encoded using the ISO 19139 and ISO 19115-3 (XML) standard
technical specifications. This includes ISO 19110 (Feature cataloguing),
19115 (dataset metadata), 19119 (service metadata) and 19136 (GML). Other
interoperable schemas from the OGC are progressively supported as well,
such as the Sensor Web Enablement (SWE) Common Data Model, the OGC GML
Coverage Implementation Schema (GMLCOV), or the OGC GML Referenceable Grid
(GMLRGRID).

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
