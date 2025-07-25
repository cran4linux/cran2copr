%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bfsMaps
%global packver   1.99.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.99.4
Release:          1%{?dist}%{?buildtag}
Summary:          Plot Maps from Switzerland by Swiss Federal Statistical Office

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-httr 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-DescTools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-httr 

%description
At the Swiss Federal Statistical Office (SFSO), spatial maps of
Switzerland are available free of charge as 'Cartographic bases for
small-scale thematic mapping'. This package contains convenience functions
to import ESRI (Environmental Systems Research Institute) shape files
using the package 'sf' and to plot them easily and quickly without having
to worry too much about the technical details. It contains utilities to
combine multiple areas to one single polygon and to find neighbours for
single regions. For any point on a map, a special locator can be used to
determine to which municipality, district or canton it belongs.

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
