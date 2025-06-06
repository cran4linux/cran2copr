%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bispdep
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Bivariate Spatial Dependence Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot >= 1.3.1
BuildRequires:    R-CRAN-sp >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spData 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-boot >= 1.3.1
Requires:         R-CRAN-sp >= 1.0
Requires:         R-methods 
Requires:         R-CRAN-spData 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-spatialreg 
Requires:         R-stats 
Requires:         R-CRAN-combinat 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 

%description
A collection of functions to test spatial autocorrelation between
variables, including Moran I, Geary C and Getis G together with scatter
plots, functions for mapping and identifying clusters and outliers,
functions associated with the moments of the previous statistics that will
allow testing whether there is bivariate spatial autocorrelation, and a
function that allows identifying (visualizing neighbours) on the map, the
neighbors of any region once the scheme of the spatial weights matrix has
been established.

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
