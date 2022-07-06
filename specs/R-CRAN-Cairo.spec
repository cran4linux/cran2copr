%global __brp_check_rpaths %{nil}
%global packname  Cairo
%global packver   1.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Graphics Device using Cairo Graphics Library for Creating High-Quality Bitmap (PNG, JPEG, TIFF), Vector (PDF, SVG, PostScript) and Display (X11 and Win32) Output

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cairo-devel >= 1.2
BuildRequires:    libXt-devel
BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
R graphics device using cairographics library that can be used to create
high-quality vector (PDF, PostScript and SVG) and bitmap output
(PNG,JPEG,TIFF), and high-quality rendering in displays (X11 and Win32).
Since it uses the same back-end for all output, copying across formats is
WYSIWYG. Files are created without the dependence on X11 or other external
programs. This device supports alpha channel (semi-transparent drawing)
and resulting images can contain transparent and semi-transparent regions.
It is ideal for use in server environments (file output) and as a
replacement for other devices that don't have Cairo's capabilities such as
alpha support or anti-aliasing. Backends are modular such that any subset
of backends is supported.

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
