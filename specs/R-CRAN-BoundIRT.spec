%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BoundIRT
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Bounded Continuous Item Response Theory Models to Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.6.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.6.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rstantools

%description
Bounded continuous data are encountered in many areas of test application.
Examples include visual analogue scales used in the measurement of
personality, mood, depression, and quality of life; item response times
from tests with item deadlines; confidence ratings; and pain intensity
ratings. Using this package, item response theory (IRT) models suitable
for bounded continuous item scores can be fitted to data within a Bayesian
framework. The package draws on posterior sampling facilities provided by
R-package 'rstan' (Stan Development Team, 2025)<https://mc-stan.org/>.
Available models include the Beta IRT model by Noel and Dauvier
(2007)<doi:10.1177/0146621605287691>, the continuous response model by
Samejima (1973)<doi:10.1007/BF03372160>, the unbounded normal model by
Mellenbergh (1994)<doi:10.1207/s15327906mbr2903_2>, and the Simplex IRT
model by Flores et al. (2020)<doi:10.1007/978-3-030-43469-4_8>. All models
can be fitted with or without zero-one inflation (Molenaar et al.,
2022)<doi:10.3102/10769986221108455>. Model fit comparisons can be
conducted using the Watanabe–Akaike information criterion (WAIC), the
deviance information criterion (DIC), and the fully marginalized
likelihood (i.e., Bayes factors).

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
