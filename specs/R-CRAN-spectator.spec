%global __brp_check_rpaths %{nil}
%global packname  spectator
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'Spectator Earth' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-sf 

%description
Provides interface to the 'Spectator Earth' API
<https://api.spectator.earth/>, mainly for obtaining the acquisition plans
and satellite overpasses for Sentinel-1, Sentinel-2 and Landsat-8
satellites. Current position and trajectory can also be obtained for a
much larger set of satellites. It is also possible to search the archive
for available images over the area of interest for a given (past) period,
get the URL links to download the whole image tiles, or alternatively to
download the image for just the area of interest based on selected
spectral bands.

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
