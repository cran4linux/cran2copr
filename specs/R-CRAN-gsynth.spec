%global __brp_check_rpaths %{nil}
%global packname  gsynth
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Synthetic Control Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-MASS >= 7.3.47
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-doRNG >= 1.8.2
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-abind >= 1.4.0
BuildRequires:    R-CRAN-future >= 1.21.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.6
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-GGally >= 1.0.1
BuildRequires:    R-CRAN-lfe >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.47
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-doRNG >= 1.8.2
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-abind >= 1.4.0
Requires:         R-CRAN-future >= 1.21.0
Requires:         R-CRAN-mvtnorm >= 1.0.6
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-GGally >= 1.0.1
Requires:         R-CRAN-lfe >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
Provides causal inference with interactive fixed-effect models. It imputes
counterfactuals for each treated unit using control group information
based on a linear interactive fixed effects model that incorporates
unit-specific intercepts interacted with time-varying coefficients. This
method generalizes the synthetic control method to the case of multiple
treated units and variable treatment periods, and improves efficiency and
interpretability. This version supports unbalanced panels and implements
the matrix completion method.

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
