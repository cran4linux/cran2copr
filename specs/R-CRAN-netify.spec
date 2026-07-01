%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netify
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Network Data Workflows

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-withr 

%description
Builds, validates, analyzes, and visualizes network data from dyadic,
event, matrix, 'igraph', and 'network' inputs. Supports cross-sectional,
longitudinal, bipartite, and multi-layer networks, with conversion helpers
for common modeling workflows and plotting utilities for exploratory
analysis. Network methods are described in Wasserman and Faust (1994,
ISBN:9780521387071), Cranmer et al. (2021) <doi:10.1017/9781316662915>,
and Minhas et al. (2022) <doi:10.1017/psrm.2021.56>.

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
