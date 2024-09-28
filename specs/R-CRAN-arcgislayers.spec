%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcgislayers
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to ArcGIS Data Services

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.5
BuildRequires:    R-CRAN-arcgisutils >= 0.2.0
BuildRequires:    R-CRAN-arcpbf >= 0.1.5
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr2 >= 1.0.5
Requires:         R-CRAN-arcgisutils >= 0.2.0
Requires:         R-CRAN-arcpbf >= 0.1.5
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonify 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Enables users of 'ArcGIS Enterprise', 'ArcGIS Online', or 'ArcGIS
Platform' to read, write, publish, or manage vector and raster data via
ArcGIS location services REST API endpoints
<https://developers.arcgis.com/rest/>.

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
