%global packname  hereR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          'sf'-Based Interface to the 'HERE' REST APIs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.2
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-sf >= 0.8.0
BuildRequires:    R-CRAN-lwgeom >= 0.1.7
Requires:         R-CRAN-curl >= 4.2
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-lwgeom >= 0.1.7

%description
Interface to the 'HERE' REST APIs
<https://developer.here.com/develop/rest-apis>: (1) geocode and
autocomplete addresses or reverse geocode POIs using the 'Geocoder' API;
(2) route directions, travel distance or time matrices and isolines using
the 'Routing' API; (3) request real-time traffic flow and incident
information from the 'Traffic' API; (4) find request public transport
connections and nearby stations from the 'Public Transit' API; (5) get
weather forecasts, reports on current weather conditions, astronomical
information and alerts at a specific location from the 'Destination
Weather' API. Locations, routes and isolines are returned as 'sf' objects.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figure
%{rlibdir}/%{packname}/INDEX
