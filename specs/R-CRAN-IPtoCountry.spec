%global packname  IPtoCountry
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Convert IP Addresses to Country Names or Full Location withGeoplotting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dtables 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-install.load 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dtables 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-install.load 

%description
Tools for identifying the origins of IP addresses. Includes functions for
converting IP addresses to country names, location details (region, city,
zip, latitude, longitude), IP codes, binary values, as well as a function
for plotting IP locations on a world map. This product includes
IP2Location LITE data available from <http://www.ip2location.com> and is
is available by Creative Commons Attribution-ShareAlike 4.0 Interational
license (CC-BY-SA 4.0).

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
