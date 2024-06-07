%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  svgtools
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate SVG (Template) Files of Charts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magick >= 2.4.0
BuildRequires:    R-CRAN-rsvg >= 2.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.0
Requires:         R-CRAN-magick >= 2.4.0
Requires:         R-CRAN-rsvg >= 2.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.0

%description
The purpose of this package is to manipulate SVG files that are templates
of charts the user wants to produce. In vector graphics one copes with
x-/y-coordinates of elements (e.g. lines, rectangles, text). Their scale
is often dependent on the program that is used to produce the graphics. In
applied statistics one usually has numeric values on a fixed scale (e.g.
percentage values between 0 and 100) to show in a chart. Basically,
'svgtools' transforms the statistical values into coordinates and
widths/heights of the vector graphics. This is done by stackedBar() for
bar charts, by linesSymbols() for charts with lines and/or symbols (dot
markers) and scatterSymbols() for scatterplots.

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
