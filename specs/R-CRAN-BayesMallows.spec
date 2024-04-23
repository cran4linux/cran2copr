%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesMallows
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Preference Learning with the Mallows Rank Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-sets >= 1.0.18
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-Rdpack >= 1.0
BuildRequires:    R-CRAN-relations >= 0.6.8
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-sets >= 1.0.18
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Rdpack >= 1.0
Requires:         R-CRAN-relations >= 0.6.8
Requires:         R-CRAN-rlang >= 0.3.1

%description
An implementation of the Bayesian version of the Mallows rank model
(Vitelli et al., Journal of Machine Learning Research, 2018
<https://jmlr.org/papers/v18/15-481.html>; Crispino et al., Annals of
Applied Statistics, 2019 <doi:10.1214/18-AOAS1203>; Sorensen et al., R
Journal, 2020 <doi:10.32614/RJ-2020-026>; Stein, PhD Thesis, 2023
<https://eprints.lancs.ac.uk/id/eprint/195759>). Both Metropolis-Hastings
and sequential Monte Carlo algorithms for estimating the models are
available. Cayley, footrule, Hamming, Kendall, Spearman, and Ulam
distances are supported in the models. The rank data to be analyzed can be
in the form of complete rankings, top-k rankings, partially missing
rankings, as well as consistent and inconsistent pairwise preferences.
Several functions for plotting and studying the posterior distributions of
parameters are provided. The package also provides functions for
estimating the partition function (normalizing constant) of the Mallows
rank model, both with the importance sampling algorithm of Vitelli et al.
and asymptotic approximation with the IPFP algorithm (Mukherjee, Annals of
Statistics, 2016 <doi:10.1214/15-AOS1389>).

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
