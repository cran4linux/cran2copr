%global packname  RSAGA
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          SAGA Geoprocessing and Terrain Analysis

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-shapefiles 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-shapefiles 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 

%description
Provides access to geocomputing and terrain analysis functions of the
geographical information system (GIS) 'SAGA' (System for Automated
Geoscientific Analyses) from within R by running the command line version
of SAGA. This package furthermore provides several R functions for
handling ASCII grids, including a flexible framework for applying local
functions (including predict methods of fitted models) and focal functions
to multiple grids. SAGA GIS is available under GPLv2 / LGPLv2 licence from
<http://sourceforge.net/projects/saga-gis/>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
