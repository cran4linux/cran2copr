%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetworkChange
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Package for Network Changepoint Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-network 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-viridis 

%description
Network changepoint analysis for undirected network data. The package
implements a hidden Markov network change point model (Park and Sohn
(2020)). Functions for break number detection using the approximate
marginal likelihood and WAIC are also provided. This version includes
performance optimizations with vectorized MCMC operations and modern
ggplot2-based visualizations with colorblind-friendly palettes.

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
