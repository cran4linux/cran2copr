%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggchord
%global packver   0.16.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.6
Release:          1%{?dist}%{?buildtag}
Summary:          Layered Chord, Circular and Linear Sequence Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
A 'ggplot2'-based package for multi-sequence alignment chord diagrams,
linear collinearity plots and single circular sequence maps. A layered
grammar combines sequence backbones, interval links, genes, general
biological features, labels, quantitative tracks, genomic axes and
restriction sites. Feature placement is expressed with reusable Position
objects, while role-specific scales and themes keep data mapping separate
from geometry and appearance.

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
