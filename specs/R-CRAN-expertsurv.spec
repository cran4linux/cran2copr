%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  expertsurv
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Incorporate Expert Opinion with Parametric Survival Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.2.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-flexsurv >= 2.0
BuildRequires:    R-CRAN-magrittr >= 2.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-SHELF 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.2.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-flexsurv >= 2.0
Requires:         R-CRAN-magrittr >= 2.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-SHELF 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
Enables users to incorporate expert opinion with parametric survival
analysis using a Bayesian or frequentist approach. Expert Opinion can be
provided on the survival probabilities at certain time-point(s) or for the
difference in mean survival between two treatment arms.Please reference
its use as Cooney, P., White, A. (2023) <doi:10.1177/0272989X221150212>.

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
