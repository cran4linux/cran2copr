%global packname  algaeClassify
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Determine Phytoplankton Functional Groups Based on FunctionalTraits

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 

%description
Verify accepted taxonomic nomenclature of phytoplankton species, assign
species to functional group classifications, and manipulate taxonomic and
functional diversity data. Possible functional classifications include
Morpho-functional group (MFG; Salmaso et al. 2015 <doi:10.1111/fwb.12520>)
and CSR (Reynolds 1988; Functional morphology and the adaptive strategies
of phytoplankton. In C.D. Sandgren (ed). Growth and reproductive
strategies of freshwater phytoplankton, 388-433. Cambridge University
Press, New York). Version 1.2.0 also includes functions to query names
using the algaebase online taxonomic database
(<https://www.algaebase.org>; <doi:10.7872/crya.v35.iss2.2014.105>). The
algaeClassify package is a product of the GEISHA (Global Evaluation of the
Impacts of Storms on freshwater Habitat and Structure of phytoplankton
Assemblages), funded by CESAB (Centre for Synthesis and Analysis of
Biodiversity) and the USGS John Wesley Powell Center for Synthesis and
Analysis, with data and other support provided by members of GLEON (Global
Lake Ecology Observation Network). This software is preliminary or
provisional and is subject to revision. It is being provided to meet the
need for timely best science. The software has not received final approval
by the U.S. Geological Survey (USGS). No warranty, expressed or implied,
is made by the USGS or the U.S. Government as to the functionality of the
software and related material nor shall the fact of release constitute any
such warranty. The software is provided on the condition that neither the
USGS nor the U.S. Government shall be held liable for any damages
resulting from the authorized or unauthorized use of the software.

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
