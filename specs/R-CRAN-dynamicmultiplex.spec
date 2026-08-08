%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynamicmultiplex
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Community Detection for Evolving Multiplex Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 2.0.0
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-igraph >= 2.0.0
Requires:         R-CRAN-clue 
Requires:         R-CRAN-rlang 

%description
Multiplex temporal community detection with customizable interlayer
coupling. Runs Louvain or Leiden community detection on each network layer
and constructs interlayer ties using Jaccard similarity, overlap
coefficient, node-strength weighted variants, or direct node identity
links, and also provides a two-stage snapshot-and-match tracker that
aligns independently detected per-layer communities across time with the
Hungarian assignment algorithm. Supports user-specified layer connectivity
via the layer_links argument, enabling adjacent-only temporal coupling
that avoids the long-range pooling problem in standard multislice
approaches.

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
