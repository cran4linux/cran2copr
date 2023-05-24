%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdacca.hp
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical and Variation Partitioning for Canonical Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 

%description
This function conducts variation partitioning and hierarchical
partitioning to calculate the unique, shared (referred as to "common") and
individual contributions of each predictor (or matrix) towards explained
variation (R-square and adjusted R-square) on canonical analysis (RDA,CCA
and db-RDA), applying the algorithm of Lai J.,Zou Y., Zhang J.,Peres-Neto
P.(2022) Generalizing hierarchical and variation partitioning in multiple
regression and canonical analyses using the rdacca.hp R package.Methods in
Ecology and Evolution,13: 782-788 <DOI:10.1111/2041-210X.13800>.

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
