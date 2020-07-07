%global packname  MazamaSpatialUtils
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          3%{?dist}
Summary:          Spatial Data Download and Utility Functions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rvest >= 0.3.0
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geojsonio 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmapshaper 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-rvest >= 0.3.0
Requires:         R-CRAN-sp 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geojsonio 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmapshaper 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-magrittr 

%description
A suite of conversion scripts to create internally standardized spatial
polygons data frames. Utility scripts use these data sets to return values
such as country, state, timezone, watershed, etc. associated with a set of
longitude/latitude pairs. (They also make cool maps.)

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny_examples
%{rlibdir}/%{packname}/INDEX
