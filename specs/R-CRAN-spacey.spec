%global __brp_check_rpaths %{nil}
%global packname  spacey
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Easily Obtain Spatial Data and Make Better Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rayshader 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rayshader 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rgdal 

%description
One of the remaining pain points in making beautiful maps via packages
like 'rayshader' is both obtaining and processing spatial data to build
from. 'spacey' aims to make it easier to obtain and use this data for
locations within the United States, providing utilities to download 'USGS'
and 'ESRI' geospatial data and quickly turn it into maps.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
