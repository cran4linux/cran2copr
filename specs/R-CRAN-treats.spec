%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  treats
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Trees and Traits Simulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-dispRity 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-dispRity 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-rgl 

%description
A modular package for simulating phylogenetic trees and species traits
jointly. Trees can be simulated using modular birth-death parameters (e.g.
changing starting parameters or algorithm rules). Traits can be simulated
in any way designed by the user. The growth of the tree and the traits can
influence each other through modifiers objects providing rules for
affecting each other. Finally, events can be created to modify both the
tree and the traits under specific conditions ( Guillerme, 2024
<DOI:10.1111/2041-210X.14306>).

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
