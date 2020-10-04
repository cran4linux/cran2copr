%global packname  trackeR
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          Infrastructure for Running, Cycling and Swimming Data fromGPS-Enabled Tracking Devices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 

%description
Provides infrastructure for handling running, cycling and swimming data
from GPS-enabled tracking devices within R. The package provides methods
to extract, clean and organise workout and competition data into
session-based and unit-aware data objects of class 'trackeRdata' (S3
class). The information can then be visualised, summarised, and analysed
through flexible and extensible methods. Frick and Kosmidis (2017) <doi:
10.18637/jss.v082.i07>, which is updated and maintained as one of the
vignettes, provides detailed descriptions of the package and its methods,
and real-data demonstrations of the package functionality.

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
%doc %{rlibdir}/%{packname}/art
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/icons
%{rlibdir}/%{packname}/INDEX
