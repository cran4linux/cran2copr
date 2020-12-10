%global packname  bpcs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Paired Comparison Analysis with Stan

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.20.0
BuildRequires:    R-CRAN-StanHeaders >= 2.20.0
BuildRequires:    R-CRAN-rstantools >= 2.1.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-shinystan 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-badger 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.20.0
Requires:         R-CRAN-rstantools >= 2.1.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-shinystan 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-badger 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rstantools

%description
Models for the analysis of paired comparison data using Stan. The models
include Bayesian versions of the Bradley-Terry model, including random
effects (1 level), generalized model for predictors, order effect (home
advantage) and the variations for the Davidson (1970) model to handle
ties. Additionally, we provide a number of functions to facilitate
inference and obtaining results with these models. References: Bradley and
Terry (1952) <doi:10.2307/2334029>; Davidson (1970)
<doi:10.1080/01621459.1970.10481082>; Carpenter et al. (2017)
<doi:10.18637/jss.v076.i01>.

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
