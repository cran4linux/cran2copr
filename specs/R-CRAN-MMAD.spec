%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MMAD
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package of Minorization-Maximization Algorithm via the Assembly--Decomposition Technology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
The minorization-maximization (MM) algorithm is a powerful tool for
maximizing nonconcave target function. However, for most existing MM
algorithms, the surrogate function in the minorization step is constructed
in a case-specific manner and requires manual programming. To address this
limitation, we develop the R package MMAD, which systematically integrates
the assembly--decomposition technology in the MM framework. This new
package provides a comprehensive computational toolkit for one-stop
inference of complex target functions, including function construction,
evaluation, minorization and optimization via MM algorithm. By
representing the target function through a hierarchical composition of
assembly functions, we design a hierarchical algorithmic structure that
supports both bottom-up operations (construction, evaluation) and top-down
operation (minorization).

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
