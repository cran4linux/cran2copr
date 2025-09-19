%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcgisutils
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          R-ArcGIS Bridge Utility Functions

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-httr2 >= 1.0.5
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yyjsonr 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-httr2 >= 1.0.5
Requires:         R-CRAN-cli 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-sf 
Requires:         R-utils 
Requires:         R-CRAN-yyjsonr 
Requires:         R-CRAN-lifecycle 

%description
Developer oriented utility functions designed to be used as the building
blocks of R packages that work with ArcGIS Location Services. It provides
functionality for authorization, Esri JSON construction and parsing, as
well as other utilities pertaining to geometry and Esri type conversions.
To support 'ArcGIS Pro' users, authorization can be done via
'arcgisbinding'. Installation instructions for 'arcgisbinding' can be
found at <https://developers.arcgis.com/r-bridge/installation/>.

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
