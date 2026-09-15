%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  combinat
%global packver   0.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Combinatorics Utilities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides routines for combinatorial enumeration including generation of
all combinations, permutations, and lattice points on hypercuboids and
simplex lattices. Includes utilities for multinomial distributions: the
multinomial probability mass function, random sampling with varying
parameters, and encoding conversions between simplex representations. Also
supplies exact and log-scale factorial computation and the generalized
binomial coefficient for real-valued n.  Package functions include
procedures described in Reingold, Nievergelt and Deo (1977) Combinatorial
Algorithms: Theory and Practice (dl.acm.org/citation.cfm?id=1096489),
Feller volume 1, and Nijenhuis and Wilf (1978) Combinatorial Algorithms
for Computers and Calculators (ISBN 0125192606 / 9780125192606).

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
