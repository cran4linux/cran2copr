%global __brp_check_rpaths %{nil}
%global packname  glmmfields
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Mixed Models with Robust Random Fields forSpatiotemporal Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-rstan >= 2.18.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-rstan >= 2.18.2
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-methods 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.mixed 
Requires:         R-cluster 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nlme 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tibble 

%description
Implements Bayesian spatial and spatiotemporal models that optionally
allow for extreme spatial deviations through time. 'glmmfields' uses a
predictive process approach with random fields implemented through a
multivariate-t distribution instead of the usual multivariate normal.
Sampling is conducted with 'Stan'. References: Anderson and Ward (2019)
<doi:10.1002/ecy.2403>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
