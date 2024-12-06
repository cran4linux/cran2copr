%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PoolTestR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prevalence and Regression for Pool-Tested (Group-Tested) Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.3.1.1
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-lme4 >= 1.1.35.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.3.1.1
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-lme4 >= 1.1.35.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-brms 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rstantools

%description
An easy-to-use tool for working with presence/absence tests on 'pooled' or
'grouped' samples. The primary application is for estimating prevalence of
a marker in a population based on the results of tests on pooled
specimens.  This sampling method is often employed in surveillance of rare
conditions in humans or animals (e.g. molecular xenomonitoring). The
package was initially conceived as an R-based alternative to the molecular
xenomonitoring software, 'PoolScreen'
<https://sites.uab.edu/statgenetics/software/>. However, it goes further,
allowing for estimates of prevalence to be adjusted for hierarchical
sampling frames, and perform flexible mixed-effect regression analyses
(McLure et al. Environmental Modelling and Software.
<DOI:10.1016/j.envsoft.2021.105158>). The package is currently in early
stages, however more features are planned or in the works: e.g.
adjustments for imperfect test specificity/sensitivity, functions for
helping with optimal experimental design, and functions for spatial
modelling.

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
