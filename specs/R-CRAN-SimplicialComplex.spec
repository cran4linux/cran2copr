%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimplicialComplex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Topological Data Analysis: Simplicial Complex

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 

%description
Provides an implementation of simplicial complexes for Topological Data
Analysis (TDA). The package includes functions to compute faces, boundary
operators, Betti numbers, Euler characteristic, and to construct
simplicial complexes. It also implements persistent homology, from
building filtrations to computing persistence diagrams, with the aim of
helping readers understand the core concepts of computational topology.
Methods are based on standard references in persistent homology such as
Zomorodian and Carlsson (2005) <doi:10.1007/s00454-004-1146-y> and Chazal
and Michel (2021) <doi:10.3389/frai.2021.667963>.

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
