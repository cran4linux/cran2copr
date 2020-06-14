%global packname  mapr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Visualize Species Occurrence Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spocc >= 0.6.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-gistr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-spocc >= 0.6.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-gistr 
Requires:         R-CRAN-data.table 

%description
Utilities for visualizing species occurrence data. Includes functions to
visualize occurrence data from 'spocc', 'rgbif', and other packages.
Mapping options included for base R plots, 'ggplot2', 'ggmap', 'leaflet'
and 'GitHub' 'gists'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
