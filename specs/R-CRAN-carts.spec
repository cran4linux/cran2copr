%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  carts
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Assessment of Covariate Adjustment in Randomized Trials

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-lava >= 1.8.0
BuildRequires:    R-CRAN-data.table >= 1.14
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-targeted >= 0.6
BuildRequires:    R-CRAN-logger >= 0.2.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-lava >= 1.8.0
Requires:         R-CRAN-data.table >= 1.14
Requires:         R-CRAN-targeted >= 0.6
Requires:         R-CRAN-logger >= 0.2.2
Requires:         R-methods 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rlang 

%description
Monte Carlo simulation framework for different randomized clinical trial
designs with a special emphasis on estimators based on covariate
adjustment. The package implements regression-based covariate adjustment
(Rosenblum & van der Laan (2010) <doi:10.2202/1557-4679.1138>) and a
one-step estimator (Van Lancker et al (2024)
<doi:10.48550/arXiv.2404.11150>) for trials with continuous, binary and
count outcomes. The estimation of the minimum sample-size required to
reach a specified statistical power for a given estimator uses bisection
to find an initial rough estimate, followed by stochastic approximation
(Robbins-Monro (1951) <doi:10.1214/aoms/1177729586>) to improve the
estimate, and finally, a grid search to refine the estimate in the
neighborhood of the current best solution.

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
