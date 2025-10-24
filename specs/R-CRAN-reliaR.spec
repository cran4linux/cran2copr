%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reliaR
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Tools for some Probability Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides a comprehensive suite of utilities for univariate continuous
probability distributions and reliability models. Includes functions to
compute the probability density, cumulative distribution, quantile,
reliability, and hazard functions, along with random variate generation.
Also offers diagnostic and model assessment tools such as
Quantile-Quantile (Q-Q) and Probability-Probability (P-P) plots, the
Kolmogorov-Smirnov goodness-of-fit test, and model selection criteria
including the Akaike Information Criterion (AIC) and Bayesian Information
Criterion (BIC). Currently implements the following distributions: Burr X,
Chen, Exponential Extension, Exponentiated Logistic, Exponentiated
Weibull, Exponential Power, Flexible Weibull, Generalized Exponential,
Gompertz, Generalized Power Weibull, Gumbel, Inverse Generalized
Exponential, Linear Failure Rate, Log-Gamma, Logistic-Exponential,
Logistic-Rayleigh, Log-log, Marshall-Olkin Extended Exponential,
Marshall-Olkin Extended Weibull, and Weibull Extension distributions.
Serves as a valuable resource for teaching and research in probability
theory, reliability analysis, and applied statistical modeling.

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
