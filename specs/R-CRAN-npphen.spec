%global packname  npphen
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Vegetation Phenological Cycle and Anomaly Detection using RemoteSensing Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rts 
BuildRequires:    R-CRAN-snow 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ks 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rts 
Requires:         R-CRAN-snow 

%description
Calculates phenological cycle and anomalies using a non-parametric
approach applied to time series of vegetation indices derived from remote
sensing data or field measurements. The package implements basic and
high-level functions for manipulating vector data (numerical series) and
raster data (satellite derived products). Processing of very large raster
files is supported.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
