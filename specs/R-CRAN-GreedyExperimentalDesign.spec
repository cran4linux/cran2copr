%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GreedyExperimentalDesign
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Greedy Experimental Design Construction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-rJava >= 0.9.6
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-nbpMatching 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-rJava >= 0.9.6
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-nbpMatching 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Computes experimental designs for two-arm experiments with covariates
using multiple methods, including: (0) complete randomization and
randomization with forced-balance; (1) greedy optimization of a balance
objective function via pairwise switching; (2) numerical optimization via
'gurobi'; (3) rerandomization; (4) Karp's method for one covariate; (5)
exhaustive enumeration for small sample sizes; (6) binary pair matching
using 'nbpMatching'; (7) binary pair matching plus method (1) to further
optimize balance; (8) binary pair matching plus method (3) to further
optimize balance; (9) Hadamard designs; and (10) simultaneous multiple
kernels. For the greedy, rerandomization, and related methods, three
objective functions are supported: Mahalanobis distance, standardized sums
of absolute differences, and kernel distances via the 'kernlab' library.
This package is the result of a stream of research that can be found in
Krieger, A. M., Azriel, D. A., and Kapelner, A. (2019). "Nearly Random
Designs with Greatly Improved Balance." Biometrika 106(3), 695-701
<doi:10.1093/biomet/asz026>. Krieger, A. M., Azriel, D. A., and Kapelner,
A. (2023). "Better experimental design by hybridizing binary matching with
imbalance optimization." Canadian Journal of Statistics, 51(1), 275-292
<doi:10.1002/cjs.11685>.

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
