%global __brp_check_rpaths %{nil}
%global packname  PosteriorBootstrap
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Parametric Sampling with Parallel Monte Carlo

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.1
BuildRequires:    R-utils >= 3.4.3
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-rstan >= 2.18.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-e1071 >= 1.7.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-MASS >= 7.3.51.1
Requires:         R-utils >= 3.4.3
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-rstan >= 2.18.2
Requires:         R-CRAN-StanHeaders >= 2.18.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-e1071 >= 1.7.1
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rstantools

%description
An implementation of a non-parametric statistical model using a
parallelised Monte Carlo sampling scheme. The method implemented in this
package allows non-parametric inference to be regularized for small sample
sizes, while also being more accurate than approximations such as
variational Bayes. The concentration parameter is an effective sample size
parameter, determining the faith we have in the model versus the data.
When the concentration is low, the samples are close to the exact Bayesian
logistic regression method; when the concentration is high, the samples
are close to the simplified variational Bayes logistic regression. The
method is described in full in the paper Lyddon, Walker, and Holmes
(2018), "Nonparametric learning from Bayesian models with randomized
objective functions" <arXiv:1806.11544>.

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
