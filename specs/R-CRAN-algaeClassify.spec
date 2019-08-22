%global packname  algaeClassify
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Determine Phytoplankton Functional Groups Based on FunctionalTraits

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch

%description
Functions designed to facilitate the assignment of morpho-functional group
(MFG) classifications to phytoplankton species based on a combination of
taxonomy (Class,Order) and a suite of 7 binomial functional traits.
Classifications can also be made using only a species list and a database
of trait-derived classifications included in the package. MFG
classifications are derived from Salmaso et al. (2015)
<doi:10.1111/fwb.12520> and this reference should be cited when using the
package. The 'algaeClassify' package is a product of the GEISHA (Global
Evaluation of the Impacts of Storms on freshwater Habitat and Structure of
phytoplankton Assemblages), funded by CESAB (Centre for Synthesis and
Analysis of Biodiversity) and the USGS John Wesley Powell Center, with
data and other support provided by members of GLEON (Global Lake Ecology
Observation Network). This software is preliminary or provisional and is
subject to revision. It is being provided to meet the need for timely best
science. The software has not received final approval by the U.S.
Geological Survey (USGS). No warranty, expressed or implied, is made by
the USGS or the U.S. Government as to the functionality of the software
and related material nor shall the fact of release constitute any such
warranty. The software is provided on the condition that neither the USGS
nor the U.S. Government shall be held liable for any damages resulting
from the authorized on unauthorized use of the software.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
