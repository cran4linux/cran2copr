%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ows4R
%global packver   0.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to OGC Web-Services (OWS)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.96.1.1
BuildRequires:    R-CRAN-geometa >= 0.7.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-parallel 
Requires:         R-CRAN-XML >= 3.96.1.1
Requires:         R-CRAN-geometa >= 0.7.1
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-parallel 

%description
Provides an Interface to Web-Services defined as standards by the Open
Geospatial Consortium (OGC), including Web Feature Service (WFS) for
vector data, Web Coverage Service (WCS), Catalogue Service (CSW) for
ISO/OGC metadata, Web Processing Service (WPS) for data processes, and
associated standards such as the common web-service specification (OWS)
and OGC Filter Encoding. Partial support is provided for the Web Map
Service (WMS). The purpose is to add support for additional OGC service
standards such as Web Coverage Processing Service (WCPS), the Sensor
Observation Service (SOS), or even new standard services emerging such OGC
API or SensorThings.

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
