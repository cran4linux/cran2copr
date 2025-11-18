%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bin2norm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Probit Estimation for Dichotomized Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-rstantools

%description
Provides likelihood-based and hierarchical estimation methods for
thresholded (binomial-probit) data. Supports fixed-mean and random-mean
models with maximum likelihood estimation (MLE), generalized linear mixed
model (GLMM), and Bayesian Markov chain Monte Carlo (MCMC)
implementations. For methodological background, see Albert and Chib (1993)
<doi:10.1080/01621459.1993.10476321> and McCulloch (1994)
<doi:10.2307/2297959>.

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
