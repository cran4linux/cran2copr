%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FPScausal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Propensity Score for Causal Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.0
BuildRequires:    R-CRAN-fda >= 6.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-patchwork >= 1.1.0
BuildRequires:    R-CRAN-wCorr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.0
Requires:         R-CRAN-fda >= 6.0.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-patchwork >= 1.1.0
Requires:         R-CRAN-wCorr 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements functional propensity score (FPS) weighting for causal
inference with functional treatments. Weights are estimated by maximising
the empirical likelihood subject to covariate-balancing constraints and
solving the resulting dual problem via the BFGS quasi-Newton algorithm,
following Ciardulli, S. and Fontana, N. (2026). The package supports
scalar, binary, and functional outcomes, as well as functional covariates.

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
