%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fhircrackr
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Handling HL7 FHIR® Resources in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-lifecycle 

%description
Useful tools for conveniently downloading FHIR resources in xml format and
converting them to R data.frames. The package uses FHIR-search to download
bundles from a FHIR server, provides functions to save and read xml-files
containing such bundles and allows flattening the bundles to data.frames
using XPath expressions. FHIR® is the registered trademark of HL7 and is
used with the permission of HL7. Use of the FHIR trademark does not
constitute endorsement of this product by HL7.

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
