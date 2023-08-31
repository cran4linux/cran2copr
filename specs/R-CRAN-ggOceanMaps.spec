%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggOceanMaps
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Plot Data on Oceanographic Maps using 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-smoothr 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-smoothr 
Requires:         R-CRAN-units 

%description
Allows plotting data on bathymetric maps using 'ggplot2'. Plotting
oceanographic spatial data is made as simple as feasible, but also
flexible for custom modifications. Data that contain geographic
information from anywhere around the globe can be plotted on maps
generated by the basemap() or qmap() functions using 'ggplot2' layers
separated by the '+' operator. The package uses spatial shape- ('sf') and
raster ('stars') files, geospatial packages for R to manipulate, and the
'ggplot2' package to plot these files. The package ships with
low-resolution spatial data files and higher resolution files for detailed
maps are stored in the 'ggOceanMapsLargeData' repository on GitHub and
downloaded automatically when needed.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
