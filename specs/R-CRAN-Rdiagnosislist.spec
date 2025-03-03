%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rdiagnosislist
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate SNOMED CT Diagnosis Lists

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-bit64 
Requires:         R-methods 

%description
Functions and methods for manipulating 'SNOMED CT' concepts. The package
contains functions for loading the 'SNOMED CT' release into a convenient R
environment, selecting 'SNOMED CT' concepts using regular expressions, and
navigating the 'SNOMED CT' ontology. It provides the 'SNOMEDconcept' S3
class for a vector of 'SNOMED CT' concepts (stored as 64-bit integers) and
the 'SNOMEDcodelist' S3 class for a table of concepts IDs with
descriptions. The package can be used to construct sets of 'SNOMED CT'
concepts for research (<doi:10.1093/jamia/ocac158>). For more information
about 'SNOMED CT' visit <https://www.snomed.org/>.

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
