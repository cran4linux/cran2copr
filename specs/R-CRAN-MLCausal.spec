%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLCausal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference Methods for Multilevel and Clustered Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-sandwich >= 3.0.0
BuildRequires:    R-CRAN-lmtest >= 0.9.38
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-sandwich >= 3.0.0
Requires:         R-CRAN-lmtest >= 0.9.38
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-stats 

%description
Provides an end-to-end workflow for estimating average treatment effects
in clustered (multilevel) observational data. Core functionality includes
cluster-aware propensity score estimation using fixed effects and
Mundlak-style specifications, inverse probability weighting,
within-cluster nearest-neighbor matching, covariate balance diagnostics at
both individual and cluster-mean levels, outcome regression with
cluster-robust standard errors, propensity score overlap visualization,
and tipping-point sensitivity analysis for omitted cluster-level
confounding.

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
