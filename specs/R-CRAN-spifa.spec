%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spifa
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatial Item Factor Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-RcppTN 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-RcppTN 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-patchwork 

%description
Fits spatial item factor analysis models for binary responses, following
Chacón-Montalván, E. A., Parry, L., Giorgi, E., Torres, P., Orellana, J.
D. Y., Moraga, P., and Taylor, B. M. (2025) <doi:10.1214/25-AOAS2072>,
using full Bayesian inference via adaptive Metropolis-Hastings within
Gibbs sampling and auxiliary variables with a probit link function. The
latent factors are modelled as the sum of a predictor effect, a
multivariate Gaussian process capturing spatial dependence, and a
multivariate non-spatial term, allowing users to fit and predict
spatially-referenced constructs such as food insecurity or socioeconomic
indices. Standard exploratory and confirmatory item factor analysis are
supported as particular cases, simply by dropping the spatial structure.

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
