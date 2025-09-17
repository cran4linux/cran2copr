%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ezTrack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploring Animal Movement Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-adehabitatHR 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-adehabitatHR 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmltools 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-dplyr 

%description
Streamlines common steps for working with animal tracking data, from raw
telemetry points to summaries, interactive maps, and home range estimates.
Designed to be beginner-friendly, it enables rapid exploration of spatial
and movement data with minimal wrangling, providing a unified workflow for
importing, summarizing, and visualizing, and analyzing animal movement
datasets.

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
