%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mapsf
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Thematic Cartography

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-maplegend 
BuildRequires:    R-CRAN-s2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-classInt 
Requires:         R-graphics 
Requires:         R-CRAN-maplegend 
Requires:         R-CRAN-s2 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Create and integrate thematic maps in your workflow. This package helps to
design various cartographic representations such as proportional symbols,
choropleth or typology maps. It also offers several functions to display
layout elements that improve the graphic presentation of maps (e.g. scale
bar, north arrow, title, labels). 'mapsf' maps 'sf' objects on 'base'
graphics.

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
