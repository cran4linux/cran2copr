%global __brp_check_rpaths %{nil}
%global packname  wux
%global packver   2.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Wegener Center Climate Uncertainty Explorer

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-class 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-rworldmap 
Requires:         R-methods 

%description
Methods to calculate and interpret climate change signals and time series
from climate multi-model ensembles. Climate model output in binary
'NetCDF' format is read in and aggregated over a specified region to a
data.frame for statistical analysis. Global Circulation Models, as the
'CMIP5' simulations, can be read in the same way as Regional Climate
Models, as e.g. the 'CORDEX' or 'ENSEMBLES' simulations. The package has
been developed at the 'Wegener Center for Climate and Global Change' at
the University of Graz, Austria.

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
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
