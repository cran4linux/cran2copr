%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsmSearch
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          DSM and LiDAR downloader

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-imager 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-imager 

%description
A collection of functions to search and donwload DSM (Digital Surface
Model) and LiDAR (Light Detection and Ranging) data via APIs, including
'OpenTopography' <https://portal.opentopography.org/apidocs/> and
'TNMAccess' <https://apps.nationalmap.gov/tnmaccess/#/>.

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
