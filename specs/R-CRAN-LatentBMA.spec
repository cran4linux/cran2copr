%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LatentBMA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Model Averaging for Univariate Link Latent Gaussian Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-mnormt >= 2.1.1
BuildRequires:    R-CRAN-knitr >= 1.47
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-progress >= 1.2.3
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-mnormt >= 2.1.1
Requires:         R-CRAN-knitr >= 1.47
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-progress >= 1.2.3

%description
Bayesian model averaging (BMA) algorithms for univariate link latent
Gaussian models (ULLGMs). For detailed information, refer to Steel M.F.J.
& Zens G. (2024) "Model Uncertainty in Latent Gaussian Models with
Univariate Link Function" <doi:10.48550/arXiv.2406.17318>. The package
supports various g-priors and a beta-binomial prior on the model space. It
also includes auxiliary functions for visualizing and tabulating BMA
results. Currently, it offers an out-of-the-box solution for model
averaging of Poisson log-normal (PLN) and binomial logistic-normal (BiL)
models. The codebase is designed to be easily extendable to other
likelihoods, priors, and link functions.

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
