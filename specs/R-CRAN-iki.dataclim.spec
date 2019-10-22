%global packname  iki.dataclim
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Consistency, Homogeneity and Summary Statistics ofClimatological Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-climdex.pcic >= 1.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-PCICt 
Requires:         R-CRAN-climdex.pcic >= 1.1.1
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-PCICt 

%description
The package offers an S4 infrastructure to store climatological station
data of various temporal aggregation scales. In-built quality control and
homogeneity tests follow the methodology from the European Climate
Assessment & Dataset project. Wrappers for climate indices defined by the
Expert Team on Climate Change Detection and Indices (ETCCDI), a quick
summary of important climate statistics and climate diagram plots provide
a fast overview of climatological characteristics of the station.

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
%{rlibdir}/%{packname}/INDEX
