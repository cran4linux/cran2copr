%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ezTrack
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Exploring Animal Movement Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-adehabitatHR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-adehabitatHR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for exploring animal tracking data, from raw telemetry
points to summaries, interactive maps, and home range estimates. It is
designed to be beginner-friendly and requires minimal data wrangling.

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
