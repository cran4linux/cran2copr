%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adiv
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Diversity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-adegraphics 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-adegraphics 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-cluster 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lpSolve 
Requires:         R-methods 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-rgl 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions, data sets and examples for the calculation of various indices
of biodiversity including species, functional and phylogenetic diversity.
Part of the indices are expressed in terms of equivalent numbers of
species. The package also provides ways to partition biodiversity across
spatial or temporal scales (alpha, beta, gamma diversities). In addition
to the quantification of biodiversity, ordination approaches are available
which rely on diversity indices and allow the detailed identification of
species, functional or phylogenetic differences between communities.

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
