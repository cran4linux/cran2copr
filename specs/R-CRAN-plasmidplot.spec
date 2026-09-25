%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plasmidplot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Quality Circular and Linear Plasmid Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-tools 
Requires:         R-utils 

%description
Draws circular and linear plasmid maps with 'grid' graphics. Features are
shown as colored arcs with optional arrowheads, callout labels that are
laid out to avoid overlap, an automatic base-pair scale, and the plasmid
name and size. A style is built from a handful of shape parameters, with
presets as named combinations of them, and the layout follows the
molecule's topology. Maps can be built up feature by feature or imported
from 'GenBank', 'EMBL', 'FASTA' and 'SnapGene' files, whose format is
detected from content rather than file extension. Restriction sites can be
located in the sequence and labeled. Ships eight visual styles, including
one inspired by the 'AngularPlasmid' JavaScript library, and seven
categorical palettes checked for colorblind safety. Palettes from other
packages can be used directly, as a color vector or as a palette function,
and checked against the same criteria.

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
