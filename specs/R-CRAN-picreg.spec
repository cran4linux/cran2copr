%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  picreg
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection using the Pivotal Information Criterion

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 

%description
Sparse regression and classification via the Pivotal Information Criterion
(PIC), an alternative to the Bayesian Information Criterion (BIC),
cross-validation, and Lasso-based tuning. The regularisation parameter is
selected from a pivotal null-distribution statistic, eliminating the need
for cross-validation and yielding sharper support recovery. Provides Fast
Iterative Shrinkage-Thresholding Algorithm (FISTA) optimisation for the
L1, Smoothly Clipped Absolute Deviation (SCAD), and Minimax Concave
Penalty (MCP) penalties across six response distributions: Gaussian,
binomial, Poisson, exponential, Gumbel, and Cox. Under standard sparsity
assumptions, the selector achieves a phase transition for exact support
recovery, analogous to results in compressed sensing. See Sardy, van
Cutsem and van de Geer (2026) <doi:10.48550/arXiv.2603.04172>.

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
