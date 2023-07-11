%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geonapi
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          'GeoNetwork' API R Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geometa 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-geometa 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-XML 

%description
Provides an R interface to the 'GeoNetwork' API
(<https://geonetwork-opensource.org/#api>) allowing to upload and publish
metadata in a 'GeoNetwork' web-application and expose it to OGC CSW.

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
