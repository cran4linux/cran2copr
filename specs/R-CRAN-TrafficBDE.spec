%global packname  TrafficBDE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Traffic Status Prediction in Urban Places using Neural NetworkModels

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-RCurl 
Requires:         R-stats 
Requires:         R-CRAN-zoo 

%description
Estimate and return either the traffic speed or the car entries in the
city of Thessaloniki using historical traffic data. It's used in transport
pilot <http://trafficstatusprediction.imet.gr/> of the 'BigDataEurope'
project <https://www.big-data-europe.eu/>. There are functions for
processing these data, training a neural network, select the most
appropriate model and predict the traffic speed or the car entries for a
selected time date.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
