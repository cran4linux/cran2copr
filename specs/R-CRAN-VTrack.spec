%global __brp_check_rpaths %{nil}
%global packname  VTrack
%global packver   1.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.21
Release:          3%{?dist}%{?buildtag}
Summary:          A Collection of Tools for the Analysis of Remote AcousticTelemetry Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-plotKML 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-intervals 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-plotKML 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-intervals 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-lubridate 

%description
Designed to facilitate the assimilation, analysis and synthesis of animal
location and movement data collected by the VEMCO suite of acoustic
transmitters and receivers. As well as database and geographic information
capabilities the principal feature of VTrack is the qualification and
identification of ecologically relevant events from the acoustic detection
and sensor data. This procedure condenses the acoustic detection database
by orders of magnitude, greatly enhancing the synthesis of acoustic
detection data.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
