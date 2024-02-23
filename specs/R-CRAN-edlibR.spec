%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  edlibR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Integration for Edlib, the C/C++ Library for Exact Pairwise Sequence Alignment using Edit (Levenshtein) Distance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-Rcpp >= 1.0.5

%description
Bindings to edlib, a lightweight performant C/C++ library for exact
pairwise sequence alignment using edit distance (Levenshtein distance).
The algorithm computes the optimal alignment path, but also can be used to
find only the start and/or end of the alignment path for convenience.
Edlib was designed to be ultrafast and require little memory, with the
capability to handle very large sequences. Three alignment methods are
supported: global (Needleman-Wunsch), infix (Hybrid Wunsch), and prefix
(Semi-Hybrid Wunsch). The original C/C++ library is described in "Edlib: a
C/C++ library for fast, exact sequence alignment using edit distance", M.
Šošić, M. Šikić, <doi:10.1093/bioinformatics/btw753>.

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
