%global packname  rnoaa
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}
Summary:          'NOAA' Weather Data from R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-hoardr >= 0.5.2
BuildRequires:    R-CRAN-isdparser >= 0.2.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-geonames 
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-hoardr >= 0.5.2
Requires:         R-CRAN-isdparser >= 0.2.0
Requires:         R-utils 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-geonames 

%description
Client for many 'NOAA' data sources including the 'NCDC' climate 'API' at
<https://www.ncdc.noaa.gov/cdo-web/webservices/v2>, with functions for
each of the 'API' 'endpoints': data, data categories, data sets, data
types, locations, location categories, and stations. In addition, we have
an interface for 'NOAA' sea ice data, the 'NOAA' severe weather inventory,
'NOAA' Historical Observing 'Metadata' Repository ('HOMR') data, 'NOAA'
storm data via 'IBTrACS', tornado data via the 'NOAA' storm prediction
center, and more.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
