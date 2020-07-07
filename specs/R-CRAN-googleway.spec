%global packname  googleway
%global packver   2.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.1
Release:          3%{?dist}
Summary:          Accesses Google Maps APIs to Retrieve Data and Plot Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.20
BuildRequires:    R-CRAN-googlePolylines >= 0.7.1
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jqr 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-jsonlite >= 0.9.20
Requires:         R-CRAN-googlePolylines >= 0.7.1
Requires:         R-CRAN-curl 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jpeg 
Requires:         R-utils 
Requires:         R-CRAN-jqr 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 

%description
Provides a mechanism to plot a 'Google Map' from 'R' and overlay it with
shapes and markers. Also provides access to 'Google Maps' APIs, including
places, directions, roads, distances, geocoding, elevation and timezone.

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
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
