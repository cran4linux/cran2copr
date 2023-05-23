%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggblend
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blending and Compositing Algebra for 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-rlang 

%description
Algebra of operations for blending, copying, adjusting, and compositing
layers in 'ggplot2'. Supports copying and adjusting the aesthetics or
parameters of an existing layer, partitioning a layer into multiple pieces
for re-composition, applying affine transformations to layers, and
combining layers (or partitions of layers) using blend modes (including
commutative blend modes, like multiply and darken). Blend mode support is
particularly useful for creating plots with overlapping groups where the
layer drawing order does not change the output; see Kindlmann and
Scheidegger (2014) <doi:10.1109/TVCG.2014.2346325>.

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
