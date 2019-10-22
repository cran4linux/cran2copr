%global packname  MUCflights
%global packver   0.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Munich Franz-Josef-Strauss Airport Pattern Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere >= 1.2.15
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-NightDay 
Requires:         R-CRAN-geosphere >= 1.2.15
Requires:         R-CRAN-XML 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-NightDay 

%description
Functions for downloading flight data from http://www.munich-airport.de
and for analyzing flight patterns.

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
%doc %{rlibdir}/%{packname}/maps
%doc %{rlibdir}/%{packname}/MUCflights.RData
%{rlibdir}/%{packname}/INDEX
