%global packname  choroplethr
%global packver   3.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.3
Release:          1%{?dist}
Summary:          Simplify the Creation of Choropleth Maps in R

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-acs 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-WDI 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-RgoogleMaps 
BuildRequires:    R-CRAN-tigris 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-acs 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-WDI 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-RgoogleMaps 
Requires:         R-CRAN-tigris 
Requires:         R-CRAN-gridExtra 

%description
Choropleths are thematic maps where geographic regions, such as states,
are colored according to some metric, such as the number of people who
live in that state. This package simplifies this process by 1. Providing
ready-made functions for creating choropleths of common maps. 2. Providing
data and API connections to interesting data sources for making
choropleths. 3. Providing a framework for creating choropleths from
arbitrary shapefiles. 4. Overlaying those maps over reference maps from
Google Maps.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
