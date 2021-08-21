%global __brp_check_rpaths %{nil}
%global packname  vrnmf
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Volume-Regularized Structured Matrix Factorization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.1
Requires:         R-core >= 3.5.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI >= 5.5.2.0
BuildRequires:    R-parallel >= 3.5.1
BuildRequires:    R-CRAN-quadprog >= 1.5
BuildRequires:    R-CRAN-ica >= 1.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-stats 
Requires:         R-CRAN-lpSolveAPI >= 5.5.2.0
Requires:         R-parallel >= 3.5.1
Requires:         R-CRAN-quadprog >= 1.5
Requires:         R-CRAN-ica >= 1.0
Requires:         R-graphics 
Requires:         R-CRAN-nnls 
Requires:         R-stats 

%description
Implements a set of routines to perform structured matrix factorization
with minimum volume constraints. The NMF procedure decomposes a matrix X
into a product C * D. Given conditions such that the matrix C is
non-negative and has sufficiently spread columns, then volume minimization
of a matrix D delivers a correct and unique, up to a scale and
permutation, solution (C, D). This package provides both an implementation
of volume-regularized NMF and "anchor-free" NMF, whereby the standard NMF
problem is reformulated in the covariance domain. This algorithm was
applied in Vladimir B. Seplyarskiy Ruslan A. Soldatov, et al. "Population
sequencing data reveal a compendium of mutational processes in the human
germ line". Science, 12 Aug 2021. <doi:10.1126/science.aba7408>. This
package interacts with data available through the 'simulatedNMF' package,
which is available in a 'drat' repository. To access this data package,
see the instructions at <https://github.com/kharchenkolab/vrnmf>. The size
of the 'simulatedNMF' package is approximately 8 MB.

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
