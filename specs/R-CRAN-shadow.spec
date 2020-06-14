%global packname  shadow
%global packver   0.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7
Release:          1%{?dist}
Summary:          Geometric Shadow Calculations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.4.0
BuildRequires:    R-CRAN-raster >= 2.4.15
BuildRequires:    R-CRAN-sp >= 1.1.1
BuildRequires:    R-CRAN-rgeos >= 0.3
BuildRequires:    R-methods 
Requires:         R-parallel >= 3.4.0
Requires:         R-CRAN-raster >= 2.4.15
Requires:         R-CRAN-sp >= 1.1.1
Requires:         R-CRAN-rgeos >= 0.3
Requires:         R-methods 

%description
Functions for calculating: (1) shadow height, (2) logical shadow flag, (3)
shadow footprint, (4) Sky View Factor and (5) radiation load. Basic
required inputs include a polygonal layer of obstacle outlines along with
their heights (i.e. "extruded polygons"), sun azimuth and sun elevation.
The package also provides functions for related preliminary calculations:
breaking polygons into line segments, determining azimuth of line
segments, shifting segments by azimuth and distance, constructing the
footprint of a line-of-sight between an observer and the sun, and creating
a 3D grid covering the surface area of extruded polygons.

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
%{rlibdir}/%{packname}/INDEX
