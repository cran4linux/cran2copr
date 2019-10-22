%global packname  spex
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Spatial Extent Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-reproj >= 0.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadmesh 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-reproj >= 0.4.0
Requires:         R-methods 
Requires:         R-CRAN-quadmesh 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
Functions to produce a fully fledged 'geo-spatial' object extent as a
'SpatialPolygonsDataFrame'. Also included are functions to generate
polygons from raster data using 'quadmesh' techniques, a round number
buffered extent, and general spatial-extent and 'raster-like' extent
helpers missing from the originating packages. Some latitude-based tools
for polar maps are included.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
