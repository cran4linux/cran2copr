%global packname  dataRetrieval
%global packver   2.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.6
Release:          2%{?dist}
Summary:          Retrieval Functions for USGS and EPA Hydrologic and WaterQuality Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.5.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate >= 1.5.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-curl 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 

%description
Collection of functions to help retrieve U.S. Geological Survey (USGS) and
U.S. Environmental Protection Agency (EPA) water quality and hydrology
data from web services. USGS web services are discovered from National
Water Information System (NWIS) <https://waterservices.usgs.gov/> and
<https://waterdata.usgs.gov/nwis>. Both EPA and USGS water quality data
are obtained from the Water Quality Portal
<https://www.waterqualitydata.us/>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
