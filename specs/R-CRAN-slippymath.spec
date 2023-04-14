%global __brp_check_rpaths %{nil}
%global packname  slippymath
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Slippy Map Tile Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-png 

%description
Provides functions for performing common tasks when working with slippy
map tile service APIs e.g. Google maps, Open Street Map, Mapbox, Stamen,
among others. Functionality includes converting from latitude and
longitude to tile numbers, determining tile bounding boxes, and
compositing tiles to a georeferenced raster image.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
