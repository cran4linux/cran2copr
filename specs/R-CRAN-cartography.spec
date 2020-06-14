%global packname  cartography
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          2%{?dist}
Summary:          Thematic Cartography

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 2.0.1
BuildRequires:    geos-devel >= 3.4.0
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-sp >= 1.2.4
BuildRequires:    R-CRAN-sf >= 0.6.4
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-slippymath 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-sp >= 1.2.4
Requires:         R-CRAN-sf >= 0.6.4
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-curl 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-slippymath 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Create and integrate maps in your R workflow. This package helps to design
cartographic representations such as proportional symbols, choropleth,
typology, flows or discontinuities maps. It also offers several features
that improve the graphic presentation of maps, for instance, map palettes,
layout elements (scale, north arrow, title...), labels or legends. See
Giraud and Lambert (2017) <doi:10.1007/978-3-319-57336-6_13>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/csv
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gpkg
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
