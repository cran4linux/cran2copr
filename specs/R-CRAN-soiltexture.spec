%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soiltexture
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Soil Texture Plot, Classification and Transformation

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-tools 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-MASS 
Requires:         R-tools 
Requires:         R-tcltk 
Requires:         R-utils 

%description
"The Soil Texture Wizard" is a set of R functions designed to produce
texture triangles (also called texture plots, texture diagrams, texture
ternary plots), classify and transform soil textures data. These functions
virtually allows to plot any soil texture triangle (classification) into
any triangle geometry (isosceles, right-angled triangles, etc.). This set
of function is expected to be useful to people using soil textures data
from different soil texture classification or different particle size
systems. Many (> 15) texture triangles from all around the world are
predefined in the package. A simple text based graphical user interface is
provided: soiltexture_gui().

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
