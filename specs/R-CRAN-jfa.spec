%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jfa
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Auditing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-rstantools >= 2.2.0
BuildRequires:    R-CRAN-extraDistr >= 1.9.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-truncdist >= 1.0.2
BuildRequires:    R-CRAN-bde >= 1.0.1.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-rstantools >= 2.2.0
Requires:         R-CRAN-extraDistr >= 1.9.1
Requires:         R-CRAN-truncdist >= 1.0.2
Requires:         R-CRAN-bde >= 1.0.1.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Provides statistical methods for auditing as implemented in JASP for Audit
(Derks et al., 2021 <doi:10.21105/joss.02733>). First, the package makes
it easy for an auditor to plan a statistical sample, select the sample
from the population, and evaluate the misstatement in the sample compliant
with international auditing standards. Second, the package provides
statistical methods for auditing data, including tests of digit
distributions and repeated values. Finally, the package includes methods
for auditing algorithms on the aspect of fairness and bias. Next to
classical statistical methodology, the package implements Bayesian
equivalents of these methods whose statistical underpinnings are described
in Derks et al. (2021) <doi:10.1111/ijau.12240>, Derks et al. (2021)
<doi:10.31234/osf.io/kzqp5>, and Derks et al. (2022)
<doi:10.31234/osf.io/8nf3e>.

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
