%global packname  CityWaterBalance
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Track Flows of Water Through an Urban System

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dataRetrieval 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EcoHydRology 
BuildRequires:    R-CRAN-geoknife 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-dataRetrieval 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EcoHydRology 
Requires:         R-CRAN-geoknife 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tgp 
Requires:         R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Retrieves data and estimates unmeasured flows of water through the urban
network. Any city may be modeled with preassembled data, but data for US
cities can be gathered via web services using this package and
dependencies 'geoknife' and 'dataRetrieval'.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
