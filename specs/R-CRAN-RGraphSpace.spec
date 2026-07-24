%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RGraphSpace
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Lightweight Interface Between 'igraph' and 'ggplot2' Graphics

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggrastr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 >= 4.0
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggrastr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lifecycle 

%description
An interface for rendering 'igraph' objects as 'ggplot2' graphics within a
normalized coordinate space. 'RGraphSpace' implements new geometries that
treat a graph as a single coherent object, synchronizing node and edge
layers under standard aesthetic mappings. Node features are resolved on
demand, supporting high-dimensional data without expanding node tables.
Spatial alignment is available at the pixel level, with node coordinates
anchored to pixel centers through a half-pixel offset, enabling precise
node positioning over external reference frames such as images and maps.

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
