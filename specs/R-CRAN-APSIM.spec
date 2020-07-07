%global packname  APSIM
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          3%{?dist}
Summary:          General Utility Functions for the 'Agricultural ProductionSystems Simulator'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-plyr >= 1.8.1
BuildRequires:    R-CRAN-lubridate >= 1.3.3
BuildRequires:    R-CRAN-stringr >= 0.6.2
BuildRequires:    R-CRAN-sirad 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-plyr >= 1.8.1
Requires:         R-CRAN-lubridate >= 1.3.3
Requires:         R-CRAN-stringr >= 0.6.2
Requires:         R-CRAN-sirad 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-RSQLite 

%description
Contains functions designed to facilitate the loading and transformation
of 'Agricultural Production Systems Simulator' output files
<https://www.apsim.info>. Input meteorological data (also known as
"weather" or "met") files can also be generated from user supplied data.

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
