%global __brp_check_rpaths %{nil}
%global packname  mfbvar
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed-Frequency Bayesian VAR Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-stochvol >= 2.0.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-stochvol >= 2.0.3
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-zoo 

%description
Functions and tools for estimation of mixed-frequency Bayesian vector
autoregressive (VAR) models. The package implements a state space-based
VAR model that handles mixed frequencies of the data as proposed by
Schorfheide and Song (2015) <doi:10.1080/07350015.2014.954707>, and
extensions thereof developed by Ankargren, Unosson and Yang (2020)
<doi:10.1515/jtse-2018-0034>, Ankargren and Joneus (2019)
<arXiv:1912.02231>, and Ankargren and Joneus (2020)
<doi:10.1016/j.ecosta.2020.05.007>. The models are estimated using Markov
Chain Monte Carlo to numerically approximate the posterior distribution.
Prior distributions that can be used include normal-inverse Wishart and
normal-diffuse priors as well as steady-state priors. Stochastic
volatility can be handled by common or factor stochastic volatility
models.

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
