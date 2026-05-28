%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qch
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Query Composite Hypotheses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Provides functions for the joint analysis of Q sets of p-values obtained
for the same list of items. This joint analysis is performed by querying a
composite hypothesis, i.e. an arbitrary complex combination of simple
hypotheses, as described in Mary-Huard et al. (2021)
<doi:10.1093/bioinformatics/btab592> and De Walsche et al.(2025) <doi:
10.1093/nargab/lqaf118>. In this approach, the Q-uplet of p-values
associated with each item is distributed as a multivariate mixture, where
each of the 2^Q components corresponds to a specific combination of simple
hypotheses. The dependence between the p-value series is considered using
a Gaussian copula function. A p-value for the composite hypothesis test is
derived from the posterior probabilities.

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
