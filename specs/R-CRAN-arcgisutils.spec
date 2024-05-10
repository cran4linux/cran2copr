%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcgisutils
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          ArcGIS Utility Functions

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-utils 

%description
Developer oriented utility functions designed to be used as the building
blocks of R packages that work with ArcGIS Location Services. It provides
functionality for authorization, Esri JSON construction and parsing, as
well as other utilities pertaining to geometry and Esri type conversions.
To support 'ArcGIS Pro' users, authorization can be done via
'arcgisbinding'. Installation instructions for 'arcgisbinding' can be
found at
<https://r.esri.com/r-bridge-site/arcgisbinding/installing-arcgisbinding.html>.

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
