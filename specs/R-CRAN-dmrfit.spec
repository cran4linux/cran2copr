%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dmrfit
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Bayesian Inference for Discrete Markov Random Fields

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 

%description
Estimation of discrete Markov random fields through the pseudo-likelihood,
for both Ising models (Ising (1925) <doi:10.1007/BF02980577>) and ordinal
Markov random fields (Marsman et al. (2025) <doi:10.1017/psy.2024.4>).
Point estimates, either maximum pseudo-likelihood or maximum a posteriori,
are obtained through a trust region optimization algorithm, with robust
standard errors from the Godambe-Huber-White (GHW, or sandwich) estimator,
for both full and constrained network structures. Bayesian inference
corrects the pseudo-posterior through coordinate rescaling (Arena and
Marsman (2026) <doi:10.48550/arXiv.2601.17205>), which matches its
covariance to the GHW covariance, and samples from it with the Fisher
adaptive Metropolis-adjusted Langevin algorithm (Titsias (2024)
<doi:10.48550/arXiv.2305.14442>). For comparison, the posterior based on
the full likelihood can also be sampled, exactly for small networks or
with the double Metropolis-Hastings algorithm (Liang (2010)
<doi:10.1080/00949650902882162>). Savage-Dickey Bayes factors test each
pairwise interaction, computed either by sampling importance resampling
(Skare et al. (2003) <doi:10.1111/1467-9469.00360>) or from the posterior
draws.

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
