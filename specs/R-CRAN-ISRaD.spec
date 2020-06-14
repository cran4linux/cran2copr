%global packname  ISRaD
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          2%{?dist}
Summary:          Tools and Data for the International Soil Radiocarbon Database

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rcrossref 
BuildRequires:    R-CRAN-pangaear 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rcrossref 
Requires:         R-CRAN-pangaear 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-stringr 

%description
This is the central location for data and tools for the development,
maintenance, analysis, and deployment of the International Soil
Radiocarbon Database (ISRaD). ISRaD was developed as a collaboration
between the U.S. Geological Survey Powell Center and the Max Planck
Institute for Biogeochemistry. This R package provides tools for accessing
and manipulating ISRaD data, compiling local data using the ISRaD data
structure, and simple query and reporting functions for ISRaD. For more
detailed information visit the ISRaD website at:
<https://soilradiocarbon.org/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
