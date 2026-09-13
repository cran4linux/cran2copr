%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  krt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Author, Validate, and Export Key Resources Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 

%description
A toolkit for creating, importing, validating, enriching, rendering, and
depositing Key Resources Tables (KRTs). A KRT lists the resources used and
generated in a study (antibodies, cell lines, organisms, chemicals,
software, datasets, protocols, and more), each paired with a persistent
identifier such as a Research Resource Identifier (RRID), a Digital Object
Identifier (DOI), a repository accession, or a catalog number, so that
resources are unambiguously identifiable and machine-actionable. The
package models resources as typed, validated records around a neutral core
schema and maps them to journal or funder output profiles, following the
FAIR (Findable, Accessible, Interoperable, Reusable) principles of
Wilkinson et al. (2016) <doi:10.1038/sdata.2016.18>. It normalizes and
optionally resolves identifiers against public registries, extracts
resources from manuscripts, and renders tables both in the STAR
(Structured, Transparent, Accessible Reporting) Methods style used by Cell
Press journals and in the style required by ASAP (Aligning Science Across
Parkinson's), with an emphasis on transparency, reproducibility, and
correct per-component licensing.

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
