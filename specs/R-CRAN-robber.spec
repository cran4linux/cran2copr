%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robber
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Using Block Model to Estimate the Robustness of Ecological Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-blockmodels >= 1.1.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GREMLINS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pammtools 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
Requires:         R-CRAN-blockmodels >= 1.1.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GREMLINS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pammtools 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-purrr 
Requires:         R-stats 

%description
Implementation of a variety of methods to compute the robustness of
ecological interaction networks with binary interactions as described in
<doi:10.1002/env.2709>. In particular, using the Stochastic Block Model
and its bipartite counterpart, the Latent Block Model to put a parametric
model on the network, allows the comparison of the robustness of networks
differing in species richness and number of interactions. It also deals
with networks that are partially sampled and/or with missing values.

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
