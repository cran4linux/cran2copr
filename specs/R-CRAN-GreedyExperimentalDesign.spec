%global packname  GreedyExperimentalDesign
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Greedy Experimental Design Construction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-GreedyExperimentalDesignJARs >= 1.0
BuildRequires:    R-CRAN-rJava >= 0.9.6
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-nbpMatching 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-GreedyExperimentalDesignJARs >= 1.0
Requires:         R-CRAN-rJava >= 0.9.6
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-nbpMatching 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-kernlab 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Computes experimental designs for a two-arm experiment with covariates via
a number of methods. (0) complete randomization and randomization with
forced-balance. (1) Greedily optimizing a balance objective function via
pairwise switching. This optimization provides lower variance for the
treatment effect estimator (and higher power) while preserving a design
that is close to complete randomization. We return all iterations of the
designs for use in a permutation test. (2) The second is via numerical
optimization (via 'gurobi' which must be installed, see
<https://www.gurobi.com/documentation/9.1/quickstart_windows/r_ins_the_r_package.html>)
a la Bertsimas and Kallus. (3) rerandomization, (4) Karp's method for one
covariate, (5) exhaustive enumeration to find the optimal solution (only
for small sample sizes) (6) Binary pair matching using the 'nbpMatching'
library (7) Binary pair matching plus (1) to further optimize balance (8)
Binary pair matching plus (3) to further optimize balance (9) Hadamard
designs We also allow for three objective functions: Mahalanobis distance,
Sum of absolute differences standardized and Kernel distances via the
'kernlab' library.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
