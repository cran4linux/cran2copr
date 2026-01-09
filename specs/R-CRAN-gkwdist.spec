%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gkwdist
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Kumaraswamy Distribution Family

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-numDeriv 

%description
Implements the five-parameter Generalized Kumaraswamy ('gkw') distribution
proposed by 'Carrasco, Ferrari and Cordeiro (2010)'
<doi:10.48550/arXiv.1004.0911> and its seven nested sub-families for
modeling bounded continuous data on the unit interval (0,1). The 'gkw'
distribution extends the Kumaraswamy distribution described by Jones
(2009) <doi:10.1016/j.stamet.2008.04.001>. Provides density, distribution,
quantile, and random generation functions, along with analytical
log-likelihood, gradient, and Hessian functions implemented in 'C++' via
'RcppArmadillo' for maximum computational efficiency. Suitable for
modeling proportions, rates, percentages, and indices exhibiting complex
features such as asymmetry, or heavy tails and other shapes not adequately
captured by standard distributions like simple Beta or Kumaraswamy.

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
