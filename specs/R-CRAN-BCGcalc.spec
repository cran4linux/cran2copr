%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BCGcalc
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Condition Gradient, Calculator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 

%description
Functions to calculate Biological Condition Gradient (BCG) using input
files with one row per sample with metric values and site classes as
columns.  A second file with the BCG Rules (example included) to define
the memberships is also needed.  The three main functions convert metric
scores to metric memberships following fuzzy set BCG Rules
(BCG.Level.Assignment), combine metric memberships to level memberships
according to BCG Rules (BCG.Level.Membership), and then assign a BCG
primary and secondary level based on level memberships
(BCG.Level.Assignment).  Originally developed as a package for use with
BCG for Puget Lowland/Willamette Valley but has been further enhanced for
use with multiple communities (benthic macroinvertebrates, fish,
periphyton, or coral) and different rule sets. Oregon and Washington
reference - "Stamp, J. and J. Gerritsen. 2018. Calibration of the
Biological Condition Gradient (BCG) for Macroinvertebrate Assemblages in
Puget Lowland/Willamette Valley Freshwater Wadeable Streams. Prepared by
Tetra Tech for the US EPA Office of Water, Office of Science and
Technology and US EPA Region 10." BCG process documentation - "USEPA.
2016. A Practitioner’s Guide to the Biological Condition Gradient - A
Framework to Describe Incremental Change in Aquatic Ecosystems. EPA
842-R-16-001. Office of Science and Technology, Washington, DC 20460."

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
