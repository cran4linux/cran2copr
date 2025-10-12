%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ACSSpack
%global packver   1.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          ACSS, Corresponding INSS, and GLP Algorithms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-MASS >= 7.3.60
BuildRequires:    R-CRAN-extraDistr >= 1.4.4
BuildRequires:    R-CRAN-HDCI >= 1.0.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-RcppArmadillo >= 0.12.6.3.0
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.60
Requires:         R-CRAN-extraDistr >= 1.4.4
Requires:         R-CRAN-HDCI >= 1.0.2
Requires:         R-stats 

%description
Allow user to run the Adaptive Correlated Spike and Slab (ACSS) algorithm,
corresponding INdependent Spike and Slab (INSS) algorithm, and Giannone,
Lenza and Primiceri (GLP) algorithm with adaptive burn-in. All of the
three algorithms are used to fit high dimensional data set with either
sparse structure, or dense structure with smaller contributions from all
predictors. The state-of-the-art GLP algorithm is in Giannone, D., Lenza,
M., & Primiceri, G. E. (2021, ISBN:978-92-899-4542-4) "Economic
predictions with big data: The illusion of sparsity". The two new
algorithms, ACSS algorithm and INSS algorithm, and the discussion on their
performance can be seen in Yang, Z., Khare, K., & Michailidis, G. (2024,
submitted to Journal of Business & Economic Statistics) "Bayesian
methodology for adaptive sparsity and shrinkage in regression".

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
