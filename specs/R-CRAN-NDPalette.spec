%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NDPalette
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Notre Dame Color Palettes for R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Provides color palettes that approximate the University of Notre Dame
brand colors, together with 'ggplot2' discrete color and fill scales. The
default palette leads with six Notre Dame brand colors that read clearly
on a white background and extends through seven former Notre Dame brand
colors, interpolating when more colors are needed than the brand supplies.
The palette is intended for statistical visualization and psychometric
analysis: the white-safe ordering keeps plotted categories legible, and
the near-white-to-navy ramps suit continuous quantities such as
correlations and factor loadings. A colorblind-friendly ordering of the
Notre Dame colors themselves (arranged so the colors stay distinguishable
under simulated deuteranopia, protanopia, and tritanopia), the former
colors as a standalone palette, the four near-white brand tints (plus six
informal soft backgrounds) for backgrounds and sequential ramps, a
reference table of every color with brand and role labels, and a
palette-preview helper are also provided. A matching R Markdown
stylesheet, built from the same colors so a report and its figures share
one brand palette, themes HTML and 'shiny' output. The colors approximate
those described in the University's branding guidelines
(<https://onmessage.nd.edu/university-branding/colors/>). This is an
independent project and is not affiliated with or endorsed by the
University of Notre Dame.

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
