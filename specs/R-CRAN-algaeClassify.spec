%global __brp_check_rpaths %{nil}
%global packname  algaeClassify
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Determine Phytoplankton Functional Groups Based on Functional Traits

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 

%description
Functions that facilitate the use of accepted taxonomic nomenclature,
collection of functional trait data, and assignment of functional group
classifications to phytoplankton species. Possible classifications include
Morpho-functional group (MFG; Salmaso et al. 2015 <doi:10.1111/fwb.12520>)
and CSR (Reynolds 1988; Functional morphology and the adaptive strategies
of phytoplankton. In C.D. Sandgren (ed). Growth and reproductive
strategies of freshwater phytoplankton, 388-433. Cambridge University
Press, New York). Versions 1.3.0 and later no longer include the
algae_search() function for querying the algaebase online taxonomic
database (www.algaebase.org). Users are advised to verify taxonomic names
directly using algaebase and cite the database in resulting publications.
Note that none of the algaeClassify authors are affiliated with algaebase
in any way. The algaeClassify package is a product of the GEISHA (Global
Evaluation of the Impacts of Storms on freshwater Habitat and Structure of
phytoplankton Assemblages), funded by CESAB (Centre for Synthesis and
Analysis of Biodiversity) and the USGS John Wesley Powell Center for
Synthesis and Analysis, with data and other support provided by members of
GLEON (Global Lake Ecology Observation Network). This software is
preliminary or provisional and is subject to revision. It is being
provided to meet the need for timely best science. The software has not
received final approval by the U.S. Geological Survey (USGS). No warranty,
expressed or implied, is made by the USGS or the U.S. Government as to the
functionality of the software and related material nor shall the fact of
release constitute any such warranty. The software is provided on the
condition that neither the USGS nor the U.S. Government shall be held
liable for any damages resulting from the authorized or unauthorized use
of the software.

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
