%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CLVTools
%global packver   0.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Customer Lifetime Value Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-optimx >= 2019.12.02
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-Formula >= 1.2.4
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-digest >= 0.6.0
BuildRequires:    R-CRAN-RcppGSL >= 0.3.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-RcppArmadillo >= 0.11.4.0.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-optimx >= 2019.12.02
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-Formula >= 1.2.4
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-digest >= 0.6.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 

%description
A set of state-of-the-art probabilistic modeling approaches to derive
estimates of individual customer lifetime values (CLV). Commonly,
probabilistic approaches focus on modelling 3 processes, i.e. individuals'
attrition, transaction, and spending process. Latent customer attrition
models, which are also known as "buy-'til-you-die models", model the
attrition as well as the transaction process. They are used to make
inferences and predictions about transactional patterns of individual
customers such as their future purchase behavior. Moreover, these models
have also been used to predict individuals’ long-term engagement in
activities such as playing an online game or posting to a social media
platform. The spending process is usually modelled by a separate
probabilistic model. Combining these results yields in lifetime values
estimates for individual customers. This package includes fast and
accurate implementations of various probabilistic models for
non-contractual settings (e.g., grocery purchases or hotel visits). All
implementations support time-invariant covariates, which can be used to
control for e.g., socio-demographics. If such an extension has been
proposed in literature, we further provide the possibility to control for
time-varying covariates to control for e.g., seasonal patterns. Currently,
the package includes the following latent attrition models to model
individuals' attrition and transaction process: [1] Pareto/NBD model
(Pareto/Negative-Binomial-Distribution), [2] the Extended Pareto/NBD model
(Pareto/Negative-Binomial-Distribution with time-varying covariates), [3]
the BG/NBD model (Beta-Gamma/Negative-Binomial-Distribution) and the [4]
GGom/NBD (Gamma-Gompertz/Negative-Binomial-Distribution). Further, we
provide an implementation of the Gamma/Gamma model to model the spending
process of individuals.

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
