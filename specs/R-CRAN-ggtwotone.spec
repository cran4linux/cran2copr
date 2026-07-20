%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggtwotone
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dual-Tone and Contrast-Aware 'ggplot2' Geoms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 4.5.2
BuildRequires:    R-grid >= 4.5.2
BuildRequires:    R-methods >= 4.5.2
BuildRequires:    R-stats >= 4.5.2
BuildRequires:    R-utils >= 4.5.2
BuildRequires:    R-CRAN-ggplot2 >= 4.0.3
BuildRequires:    R-CRAN-colorspace >= 2.1.2
BuildRequires:    R-CRAN-farver >= 2.1.2
BuildRequires:    R-CRAN-tidyr >= 1.3.2
BuildRequires:    R-CRAN-rlang >= 1.1.7
Requires:         R-grDevices >= 4.5.2
Requires:         R-grid >= 4.5.2
Requires:         R-methods >= 4.5.2
Requires:         R-stats >= 4.5.2
Requires:         R-utils >= 4.5.2
Requires:         R-CRAN-ggplot2 >= 4.0.3
Requires:         R-CRAN-colorspace >= 2.1.2
Requires:         R-CRAN-farver >= 2.1.2
Requires:         R-CRAN-tidyr >= 1.3.2
Requires:         R-CRAN-rlang >= 1.1.7

%description
Provides dual-stroke and contrast-aware extensions to 'ggplot2', designed
for improved visibility and accessibility in complex visualizations.
Includes geoms for dual-stroke segments, regression lines, curved
annotations, function plots, paths, and adaptive text. Also includes
utility functions for computing contrast-aware color pairs and
perceptually distinct highlight palettes using Web Content Accessibility
Guidelines (WCAG)-based contrast logic.

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
