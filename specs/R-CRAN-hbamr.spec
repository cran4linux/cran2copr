%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hbamr
%global packver   2.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Bayesian Aldrich-McKelvey Scaling via 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.4
BuildRequires:    R-CRAN-StanHeaders >= 2.26.22
BuildRequires:    R-CRAN-rstan >= 2.26.1
BuildRequires:    R-CRAN-rstantools >= 2.2.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.1
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.1.4
Requires:         R-CRAN-rstan >= 2.26.1
Requires:         R-CRAN-rstantools >= 2.2.0
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rstantools

%description
Perform hierarchical Bayesian Aldrich-McKelvey scaling using Hamiltonian
Monte Carlo via 'Stan'. Aldrich-McKelvey ('AM') scaling is a method for
estimating the ideological positions of survey respondents and political
actors on a common scale using positional survey data. The hierarchical
versions of the Bayesian 'AM' model included in this package outperform
other versions both in terms of yielding meaningful posterior
distributions for respondent positions and in terms of recovering true
respondent positions in simulations. The package contains functions for
preparing data, fitting models, extracting estimates, plotting key
results, and comparing models using cross-validation. The original version
of the default model is described in Bølstad (2024)
<doi:10.1017/pan.2023.18>.

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
