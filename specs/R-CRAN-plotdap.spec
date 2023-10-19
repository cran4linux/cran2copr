%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plotdap
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Visualize Data from 'ERDDAP' Servers via the 'rerddap' Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-rerddap >= 0.8.0
BuildRequires:    R-CRAN-cmocean 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-rerddap >= 0.8.0
Requires:         R-CRAN-cmocean 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 

%description
Easily visualize and animate 'tabledap' and 'griddap' objects obtained via
the 'rerddap' package in a simple one-line command, using either base
graphics or 'ggplot2' graphics. 'plotdap' handles extracting and reshaping
the data, map projections and continental outlines.  Optionally the data
can be animated through time using the 'gganmiate' package.

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
