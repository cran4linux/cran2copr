%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  couplr
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Pairing and Matching via Linear Assignment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-methods 

%description
Solves optimal pairing and matching problems using linear assignment
algorithms. Provides implementations of the Hungarian method (Kuhn 1955)
<doi:10.1002/nav.3800020109>, Jonker-Volgenant shortest path algorithm
(Jonker and Volgenant 1987) <doi:10.1007/BF02278710>, Auction algorithm
(Bertsekas 1988) <doi:10.1007/BF02186476>, cost-scaling (Goldberg and
Kennedy 1995) <doi:10.1007/BF01585996>, scaling algorithms (Gabow and
Tarjan 1989) <doi:10.1137/0218069>, push-relabel (Goldberg and Tarjan
1988) <doi:10.1145/48014.61051>, and Sinkhorn entropy-regularized
transport (Cuturi 2013) <doi:10.48550/arxiv.1306.0895>. Designed for
matching plots, sites, samples, or any pairwise optimization problem.
Supports rectangular matrices, forbidden assignments, data frame inputs,
batch solving, k-best solutions, and pixel-level image morphing for
visualization. Includes automatic preprocessing with variable health
checks, multiple scaling methods (standardized, range, robust), greedy
matching algorithms, and comprehensive balance diagnostics for assessing
match quality using standardized differences and distribution comparisons.

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
