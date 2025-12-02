%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  algaeClassify
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Query the 'Algaebase' Online Database, Standardize Phytoplankton Taxonomic Data, and Perform Functional Group Classifications

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ritis 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 
Requires:         R-CRAN-ritis 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 

%description
Functions that facilitate the use of accepted taxonomic nomenclature,
collection of functional trait data, and assignment of functional group
classifications to phytoplankton species. Possible classifications include
Morpho-functional group (MFG; Salmaso et al. 2015 <doi:10.1111/fwb.12520>)
and CSR (Reynolds 1988; Functional morphology and the adaptive strategies
of phytoplankton. In C.D. Sandgren (ed). Growth and reproductive
strategies of freshwater phytoplankton, 388-433. Cambridge University
Press, New York). Versions 2.0.0 and later includes new functions for
querying the 'algaebase' online taxonomic database (www.algaebase.org),
however these functions require a valid API key that must be acquired from
the 'algaebase' administrators. Note that none of the 'algaeClassify'
authors are affiliated with 'algaebase' in any way. Taxonomic names can
also be checked against a variety of taxonomic databases using the 'Global
Names Resolver' service via its API
(<https://resolver.globalnames.org/api>). In addition, currently accepted
and outdated synonyms, and higher taxonomy, can be extracted for lists of
species from the 'ITIS' database using wrapper functions for the ritis
package. The 'algaeClassify' package is a product of the GEISHA (Global
Evaluation of the Impacts of Storms on freshwater Habitat and Structure of
phytoplankton Assemblages), funded by CESAB (Centre for Synthesis and
Analysis of Biodiversity) and the U.S. Geological Survey John Wesley
Powell Center for Synthesis and Analysis, with data and other support
provided by members of GLEON (Global Lake Ecology Observation Network).
DISCLAIMER: This software has been approved for release by the U.S.
Geological Survey (USGS). Although the software has been subjected to
rigorous review, the USGS reserves the right to update the software as
needed pursuant to further analysis and review. No warranty, expressed or
implied, is made by the USGS or the U.S. Government as to the
functionality of the software and related material nor shall the fact of
release constitute any such warranty. Furthermore, the software is
released on condition that neither the USGS nor the U.S. Government shall
be held liable for any damages resulting from its authorized or
unauthorized use.

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
