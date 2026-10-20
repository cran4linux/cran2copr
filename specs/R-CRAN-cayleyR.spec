%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cayleyR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cayley Graph Analysis for Permutation Puzzles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 

%description
Analyzes Cayley graphs of permutation puzzles. Any puzzle whose moves
permute a fixed set of positions can be declared as a permutation group,
and the same tools then work on it: cycle detection, state space
exploration and path search. Two puzzles are built in: TopSpin and Rubik's
cubes of any size. The 3x3x3 is solved by four human methods and by a
two-phase search after Herbert Kociemba; the 4x4x4 is solved by reduction.
The Iterative Cycle Intersection (ICI) method is described in Yuri
Baramykov (2026) <doi:10.48550/arXiv.2607.13219>.

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
