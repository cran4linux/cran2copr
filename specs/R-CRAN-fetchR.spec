%global packname  fetchR
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Calculate Wind Fetch

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-plotKML 
BuildRequires:    R-utils 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-plotKML 
Requires:         R-utils 

%description
Wind fetch is the unobstructed length of water over which wind can blow
from a certain direction. The wind fetch is typically calculated for many
directions around the compass rose for a given location, which can then be
incorporated into a larger model (such as the InVEST coastal vulnerability
model;
<http://data.naturalcapitalproject.org/invest-releases/documentation/2_2_0/coastal_vulnerability.html>),
or simply averaged for a reasonable measure of the overall wind exposure
for a specific marine location. The process of calculating wind fetch can
be extremely time-consuming and tedious, particularly if a large number of
fetch vectors are required at many locations. The 'fetchR' package
calculates wind fetch and summarises the information efficiently. There
are also plot methods to help visualise the wind exposure at the various
locations, and methods to output the fetch vectors to a KML file for
further investigation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
