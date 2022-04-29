%global __brp_check_rpaths %{nil}
%global packname  diffeRenTES
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of TES-Based Cell Differentiation Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-BoolNet 
BuildRequires:    R-CRAN-DOT 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-tools 
Requires:         R-CRAN-BoolNet 
Requires:         R-CRAN-DOT 
Requires:         R-CRAN-igraph 
Requires:         R-tools 

%description
Computes the ATM (Attractor Transition Matrix) structure and the tree-like
structure describing the cell differentiation process (based on the
Threshold Ergodic Set concept introduced by Serra and Villani), starting
from the Boolean networks with synchronous updating scheme of the
'BoolNet' R package. TESs (Threshold Ergodic Sets) are the mathematical
abstractions that represent the different cell types arising during
ontogenesis. TESs and the powerful model of biological differentiation
based on Boolean networks to which it belongs have been firstly described
in "A Dynamical Model of Genetic Networks for Cell Differentiation"
Villani M, Barbieri A, Serra R (2011) A Dynamical Model of Genetic
Networks for Cell Differentiation. PLOS ONE 6(3): e17703.

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
