%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  postlink
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Post-Linkage Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.5.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-label.switching 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.5.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-label.switching 
Requires:         R-methods 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-rstantools

%description
Provides a suite of statistical tools for post-linkage data analysis
(PLDA), designed to account for record linkage errors in downstream
modeling. The package implements a familiar, formula-based regression
interface that adjusts for linkage uncertainty, accommodating workflows
where direct access to unlinked primary files is restricted. It
consolidates diverse adjustment methodologies, all of which support
generalized linear models (linear, logistic, Poisson, and Gamma). These
methodologies include weighting approaches (Chambers (2009)
<https://hdl.handle.net/10779/uow.27788247>; Chambers et al. (2023)
<doi:10.1002/wics.1596>), mixture modeling (Slawski et al. (2025)
<doi:10.1093/jrsssa/qnae083>), and Bayesian mixture modeling (Gutman et
al. (2016) <doi:10.1002/sim.6586>). For time-to-event data, both the
weighting (Vo et al. (2024) <doi:10.1002/sim.9960>) and mixture modeling
approaches accommodate Cox proportional hazards models, while the Bayesian
approaches extend to parametric survival analysis. Additionally, the
package leverages mixture modeling for contingency table analyses and
Bayesian methods to enable the multiple imputation of latent match status.

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
