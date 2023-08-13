%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DivInsight
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diversity Index Calculation & Visualisation for Taxa and Location

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgbif 
Requires:         R-stats 
Requires:         R-graphics 

%description
Repurpose occurrence data for calculating diversity index values, creating
visuals, and generating species composition matrices for a chosen taxon
and location.

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
