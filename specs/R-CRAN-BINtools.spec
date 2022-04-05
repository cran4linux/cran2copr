%global __brp_check_rpaths %{nil}
%global packname  BINtools
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian BIN (Bias, Information, Noise) Model of Forecasting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-stringi >= 1.4.6
BuildRequires:    R-CRAN-mvtnorm >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-combinat >= 0.0.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-stringi >= 1.4.6
Requires:         R-CRAN-mvtnorm >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-combinat >= 0.0.8
Requires:         R-methods 
Requires:         R-CRAN-rstantools 
Requires:         R-CRAN-rstantools

%description
A recently proposed Bayesian BIN model disentangles the underlying
processes that enable forecasters and forecasting methods to improve,
decomposing forecasting accuracy into three components: bias, partial
information, and noise. By describing the differences between two groups
of forecasters, the model allows the user to carry out useful inference,
such as calculating the posterior probabilities of the treatment reducing
bias, diminishing noise, or increasing information. It also provides
insight into how much tamping down bias and noise in judgment or enhancing
the efficient extraction of valid information from the environment
improves forecasting accuracy. This package provides easy access to the
BIN model. For further information refer to the paper Ville A. Satopää,
Marat Salikhov, Philip E. Tetlock, and Barbara Mellers (2021) "Bias,
Information, Noise: The BIN Model of Forecasting"
<doi:10.1287/mnsc.2020.3882>.

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
