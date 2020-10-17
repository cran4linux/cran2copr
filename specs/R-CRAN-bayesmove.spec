%global packname  bayesmove
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Parametric Bayesian Analyses of Animal Movement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-MCMCpack >= 1.4.5
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-future >= 1.15.1
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-tictoc >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-furrr >= 0.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-MCMCpack >= 1.4.5
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-future >= 1.15.1
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-tictoc >= 1.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-furrr >= 0.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
Methods for assessing animal movement from telemetry and biologging data
using non-parametric Bayesian methods. This includes features for pre-
processing and analysis of data, as well as the visualization of results
from the models. This framework does not rely on standard parametric
density functions, which provides flexibility during model fitting.

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
