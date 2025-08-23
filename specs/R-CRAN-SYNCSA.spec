%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SYNCSA
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Functional and Phylogenetic Patterns in Metacommunities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 

%description
Analysis of metacommunities based on functional traits and phylogeny of
the community components. The functions that are offered here implement
for the R environment methods that have been available in the 'SYNCSA'
application written in C++ (by Valerio Pillar, available at
<http://ecoqua.ecologia.ufrgs.br/SYNCSA.html>).

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
