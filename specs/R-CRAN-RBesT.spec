%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RBesT
%global packver   1.8-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Bayesian Evidence Synthesis Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       pandoc
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.4.0
BuildRequires:    R-CRAN-rstan >= 2.32.0
BuildRequires:    R-CRAN-StanHeaders >= 2.32.0
BuildRequires:    R-CRAN-BH >= 1.72.0
BuildRequires:    R-CRAN-bayesplot >= 1.4.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.4.0
Requires:         R-CRAN-rstan >= 2.32.0
Requires:         R-CRAN-bayesplot >= 1.4.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rstantools

%description
Tool-set to support Bayesian evidence synthesis.  This includes
meta-analysis, (robust) prior derivation from historical data, operating
characteristics and analysis (1 and 2 sample cases). Please refer to Weber
et al. (2021) <doi:10.18637/jss.v100.i19> for details on applying this
package while Neuenschwander et al. (2010) <doi:10.1177/1740774509356002>
and Schmidli et al. (2014) <doi:10.1111/biom.12242> explain details on the
methodology.

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
