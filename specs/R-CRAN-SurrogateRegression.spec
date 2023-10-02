%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurrogateRegression
%global packver   0.6.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Surrogate Outcome Regression Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Performs estimation and inference on a partially missing target outcome
(e.g. gene expression in an inaccessible tissue) while borrowing
information from a correlated surrogate outcome (e.g. gene expression in
an accessible tissue). Rather than regarding the surrogate outcome as a
proxy for the target outcome, this package jointly models the target and
surrogate outcomes within a bivariate regression framework. Unobserved
values of either outcome are treated as missing data. In contrast to
imputation-based inference, no assumptions are required regarding the
relationship between the target and surrogate outcomes. Estimation in the
presence of bilateral outcome missingness is performed via an expectation
conditional maximization either algorithm. In the case of unilateral
target missingness, estimation is performed using an accelerated least
squares procedure. A flexible association test is provided for evaluating
hypotheses about the target regression parameters. For additional details,
see: McCaw ZR, Gaynor SM, Sun R, Lin X: "Leveraging a surrogate outcome to
improve inference on a partially missing target outcome"
<doi:10.1111/biom.13629>.

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
