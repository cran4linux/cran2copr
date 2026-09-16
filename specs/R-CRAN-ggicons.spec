%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggicons
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Icon Geometries for 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-icons >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-grImport2 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-icons >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-grid 
Requires:         R-CRAN-grImport2 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-vctrs 

%description
Provides icon geometries for 'ggplot2', using vector icon sets from the
'icons' package. Icons can be drawn as points in place of ordinary
markers, styled with the usual colour, size, alpha and angle aesthetics,
and mapped from discrete values or passed through directly. Icons also
appear in legend keys, as fixed-position annotations, and as axis, strip
and legend labels. Pictograms extend this to isotype-style unit charts,
waffle/percentage charts and rating widgets, encoding a value as a grid of
repeated icons.

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
