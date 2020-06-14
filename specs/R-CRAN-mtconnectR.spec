%global packname  mtconnectR
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Read Data from Delimited 'MTConnect' Data Files and Perform someAnalysis

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-XML >= 3.98
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-proxy 

%description
Read data in the 'MTConnect'<http://www.mtconnect.org/> standard. You can
use the package to read data from historical 'MTConnect logs' along with
the 'devices.xml' describing the device. The data is organised into a
'MTConnectDevice' S4 data structure and some convenience methods are also
provided for basic read/view operations. The package also includes some
functions for analysis of 'MTConnect' data. This includes functions to
simulate data (primarily position data, feed rate and velocities) based on
the G code and visualisation functions to compare the actual and simulated
data.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/gcode_dict.csv
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
