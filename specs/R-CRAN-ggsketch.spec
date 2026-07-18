%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggsketch
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Grammar-Native Hand-Drawn Geoms for 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-grDevices 
Requires:         R-grid 

%description
Provides 'ggplot2' geoms that render with a hand-drawn, sketchy aesthetic:
roughened strokes, double-pass lines, and hachure, cross-hatch, zigzag,
and dots fill patterns. Implemented as pure-R 'grid' grobs wrapped in
'ggproto' geoms, composable with aes(), stats, scales, and faceting. Works
on every R graphics device (PDF, PNG, SVG, screen) with no browser
dependency. Algorithms are reimplemented from the published 'rough.js'
algorithm description (Shihn, 2020,
<https://shihn.ca/posts/2020/roughjs-algorithms/>) and Wood and others
(2012, <doi:10.1109/TVCG.2012.262>); see the NOTICE file in the package
sources for attribution.

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
