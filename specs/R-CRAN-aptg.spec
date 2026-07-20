%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aptg
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Phylogenetic Tree Generator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-rotl 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-rotl 
Requires:         R-CRAN-taxize 
Requires:         R-stats 

%description
Generates phylogenetic trees and distance matrices from a list of taxon
names, or from a higher taxon expanded down to a chosen lower rank. Trees
are obtained as induced subtrees of the Open Tree of Life synthetic tree
using the 'rotl' package (Michonneau, Brown and Winter, 2016,
<doi:10.1111/2041-210X.12593>). Expansion of a higher taxon to its
descendants uses 'taxize' (Chamberlain and Szocs, 2013,
<doi:10.12688/f1000research.2-191.v2>).

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
