%global packname  metScanR
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Find, Map, and Gather Environmental Data and Metadata

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-utils 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-leaflet 
Requires:         R-grDevices 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RCurl 
Requires:         R-utils 

%description
A tool for locating, mapping, and gathering environmental data and
metadata, worldwide.  Users can search for and filter metadata from >
157,000 environmental monitoring stations among 219 countries/territories
and >20 networks/organizations via elevation, location, active dates,
elements measured (e.g., temperature, precipitation), country, network,
and/or known identifier. Future updates to the package will allow the user
to obtain datasets from stations within the database.

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
%{rlibdir}/%{packname}/INDEX
