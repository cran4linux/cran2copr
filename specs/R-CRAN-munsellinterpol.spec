%global __brp_check_rpaths %{nil}
%global packname  munsellinterpol
%global packver   3.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolate Munsell Renotation Data from Hue/Chroma to CIE/RGB

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-spacesRGB 
BuildRequires:    R-CRAN-spacesXYZ 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-spacesRGB 
Requires:         R-CRAN-spacesXYZ 

%description
Methods for interpolating data in the Munsell color system following the
ASTM D-1535 standard. Hues and chromas with decimal values can be
interpolated and converted to/from the Munsell color system and CIE xyY,
CIE XYZ, CIE Lab, CIE Luv, or RGB.  Includes ISCC-NBS color block lookup.
Based on the work by Paul Centore, "The Munsell and Kubelka-Munk Toolbox".

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
