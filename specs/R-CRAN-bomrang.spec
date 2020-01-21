%global packname  bomrang
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Australian Government Bureau of Meteorology ('BOM') Data Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.8
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-janitor >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 2.8
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-janitor >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-crayon 
Requires:         R-foreign 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rvest 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides functions to interface with Australian Government Bureau of
Meteorology ('BOM') data, fetching data and returning a tidy data frame of
precis forecasts, historical and current weather data from stations,
agriculture bulletin data, 'BOM' 0900 or 1500 weather bulletins and
downloading and importing radar and satellite imagery files.  Data (c)
Australian Government Bureau of Meteorology Creative Commons (CC)
Attribution 3.0 licence or Public Access Licence (PAL) as appropriate.
See <http://www.bom.gov.au/other/copyright.shtml> for further details.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/error_images
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/paper
%doc %{rlibdir}/%{packname}/vector
%{rlibdir}/%{packname}/INDEX
