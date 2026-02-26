%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unityForest
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Improving Interaction Modelling and Interpretability in Random Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 

%description
Implementation of the unity forest (UFO) framework (Hornung & Hapfelmeier,
2026, <doi:10.48550/arXiv.2601.07003>). UFOs are a random forest variant
designed to better take covariates with purely interaction-based effects
into account, including interactions for which none of the involved
covariates exhibits a marginal effect. While this framework tends to
improve discrimination and predictive accuracy compared to standard random
forests, it also facilitates the identification and interpretation of
(marginal or interactive) effects: In addition to the UFO algorithm for
tree construction, the package includes the unity variable importance
measure (unity VIM), which quantifies covariate effects under the
conditions in which they are strongest - either marginally or within
subgroups defined by interactions - as well as covariate-representative
tree roots (CRTRs) that provide interpretable visualizations of these
conditions. Categorical and continuous outcomes are supported. This
package is a fork of the R package 'ranger' (main author: Marvin N.
Wright), which implements random forests using an efficient C++ backend.

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
