%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  palettome
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchy-Aware, Interactively Editable Color Palettes for Clusters

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-farver 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 

%description
Assigns perceptually-informed color palettes to clustered data (e.g.
scRNA-seq clusters / cell subtypes from 'Seurat' or plain UMAP coordinate
tables), where clusters that belong to the same "family" (e.g. subtypes of
T cells) can be colored either harmoniously (shared hue, varying shade) or
with maximal contrast (with family membership encoded via a secondary
channel). Families can be auto-detected from embedding-space hierarchical
clustering or supplied explicitly, and every generated color remains
individually overridable, with manual overrides preserved across
regeneration. Colors are constructed in the HCL space as in Zeileis et al.
(2020) <doi:10.18637/jss.v096.i01>, separated using the CIEDE2000 color
difference of Sharma, Wu and Dalal (2005) <doi:10.1002/col.20070>, and
checked for color-vision deficiency using the simulation of Machado,
Oliveira and Fernandes (2009) <doi:10.1109/TVCG.2009.113>. Core algorithms
have no UI dependencies; an optional interactive 'shiny' UI is provided
separately.

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
