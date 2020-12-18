%global packname  pflamelet
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Persistence Flamelets: Computation and Inferential Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-TDA 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-TDA 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-pbapply 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-abind 

%description
Computes the Persistence Flamelets, a statistical tool for exploring the
Topological Invariants of Scale-Space families introduced in Padellini and
Brutti (2017) "Persistence Flamelets: multiscale Persistent Homology for
kernel density exploration" <arXiv:1709.07097>. Flamelets can be built
from either sub/super level sets of arbitrary functions or from a
precomputed list of Persistence Diagrams. In addition, this package
provides functions to compute confidence bands for a Flamelet via
bootstrap, assess significance of each feature, clean a Flamelet from
topological noise, perform a two sample permutation test for groups of
Flamelets and it also implements a topological heuristic for bandwidth
selection for kernel density estimators.

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
