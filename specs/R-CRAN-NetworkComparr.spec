%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetworkComparr
%global packver   0.0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Comparison of Networks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-networktools 
BuildRequires:    R-CRAN-gdata 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-networktools 
Requires:         R-CRAN-gdata 

%description
A permutation-based hypothesis test for statistical comparison of two
networks based on the invariance measures of the R package
'NetworkComparisonTest' by van Borkulo et al. (2022),
<doi:10.1037/met0000476>: network structure invariance, global strength
invariance, edge invariance, and various centrality measures. Edgelists
from dependent or independent samples are used as input. These edgelists
are generated from concept maps and summed into two comparable group
networks. The networks can be directed or undirected.

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
