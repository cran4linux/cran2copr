%global packname  GADMTools
%global packver   3.8-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.8.1
Release:          3%{?dist}
Summary:          Easy Use of 'GADM' Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rosm 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-prettymapr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rgdal 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rosm 
Requires:         R-lattice 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-prettymapr 

%description
Manipulate, assemble, export <https://gadm.org/> maps. Create
'choropleth', 'isopleth', dots plot, proportional dots, dot-density and
more.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
