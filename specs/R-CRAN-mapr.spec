%global __brp_check_rpaths %{nil}
%global packname  mapr
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-gistr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-spocc >= 0.6.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-gistr 
Requires:         R-CRAN-data.table 

%description
Utilities for visualizing species occurrence data. Includes functions to
visualize occurrence data from 'spocc', 'rgbif', and other packages.
Mapping options included for base R plots, 'ggplot2', 'leaflet' and
'GitHub' 'gists'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
