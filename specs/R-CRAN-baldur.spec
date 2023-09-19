%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baldur
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Hierarchical Modeling for Label-Free Proteomics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-rstantools >= 2.2.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-stringr >= 1.0.4
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-viridisLite >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-multidplyr >= 0.1.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-rstantools >= 2.2.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-stringr >= 1.0.4
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-viridisLite >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-multidplyr >= 0.1.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rstantools

%description
Statistical decision in proteomics data using a hierarchical Bayesian
model. There are two regression models for describing the mean-variance
trend, a gamma regression or a latent gamma mixture regression. The
regression model is then used as an Empirical Bayes estimator for the
prior on the variance in a peptide. Further, it assumes that each
measurement has an uncertainty (increased variance) associated with it
that is also inferred. Finally, it tries to estimate the posterior
distribution (by Hamiltonian Monte Carlo) for the differences in means for
each peptide in the data. Once the posterior is inferred, it integrates
the tails to estimate the probability of error from which a statistical
decision can be made. See Berg and Popescu for details
(<doi:10.1101/2023.05.11.540411>).

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
