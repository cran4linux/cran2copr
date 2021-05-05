%global packname  colorspace
%global packver   2.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for Manipulating and Assessing Colors and Palettes

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Carries out mapping between assorted color spaces including RGB, HSV, HLS,
CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB, and polar CIELAB. Qualitative,
sequential, and diverging color palettes based on HCL colors are provided
along with corresponding ggplot2 color scales. Color palette choice is
aided by an interactive app (with either a Tcl/Tk or a shiny graphical
user interface) and shiny apps with an HCL color picker and a color vision
deficiency emulator. Plotting functions for displaying and assessing
palettes include color swatches, visualizations of the HCL space, and
trajectories in HCL and/or RGB spectrum. Color manipulation functions
include: desaturation, lightening/darkening, mixing, and simulation of
color vision deficiencies (deutanomaly, protanomaly, tritanomaly). Details
can be found on the project web page at
<https://colorspace.R-Forge.R-project.org/> and in the accompanying
scientific paper: Zeileis et al. (2020, Journal of Statistical Software,
<doi:10.18637/jss.v096.i01>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
