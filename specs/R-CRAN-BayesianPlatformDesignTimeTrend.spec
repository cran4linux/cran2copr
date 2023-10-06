%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianPlatformDesignTimeTrend
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate and Analyse Bayesian Platform Trial with Time Trend

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-directlabels >= 2023.8.25
BuildRequires:    R-CRAN-rstantools >= 2.3.0
BuildRequires:    R-CRAN-rstan >= 2.26.1
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-laGP >= 1.5.9
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-BiocManager >= 1.30.19
BuildRequires:    R-CRAN-boot >= 1.3.28
BuildRequires:    R-CRAN-lhs >= 1.1.6
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-iterators >= 1.0.13
BuildRequires:    R-CRAN-reshape >= 0.8.8
BuildRequires:    R-CRAN-matrixStats >= 0.61.0
BuildRequires:    R-CRAN-ggpubr >= 0.4.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-directlabels >= 2023.8.25
Requires:         R-CRAN-rstantools >= 2.3.0
Requires:         R-CRAN-rstan >= 2.26.1
Requires:         R-CRAN-laGP >= 1.5.9
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-BiocManager >= 1.30.19
Requires:         R-CRAN-boot >= 1.3.28
Requires:         R-CRAN-lhs >= 1.1.6
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-iterators >= 1.0.13
Requires:         R-CRAN-reshape >= 0.8.8
Requires:         R-CRAN-matrixStats >= 0.61.0
Requires:         R-CRAN-ggpubr >= 0.4.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Simulating the sequential multi-arm multi-stage or platform trial with
Bayesian approach using the 'rstan' package, which provides the R
interface for the Stan. This package supports fixed ratio and Bayesian
adaptive randomization approaches for randomization. Additionally, it
allows for the study of time trend problems in platform trials. There are
demos available for a multi-arm multi-stage trial with two different null
scenarios, as well as for Bayesian trial cutoff screening. The Bayesian
adaptive randomisation approaches are described in: Trippa et al. (2012)
<doi:10.1200/JCO.2011.39.8420> and Wathen et al. (2017)
<doi:10.1177/1740774517692302>. The randomisation algorithm is described
in: Zhao W <doi:10.1016/j.cct.2015.06.008>. The analysis methods of time
trend effect in platform trial are described in: Saville et al. (2022)
<doi:10.1177/17407745221112013> and Bofill Roig et al. (2022)
<doi:10.1186/s12874-022-01683-w>.

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
