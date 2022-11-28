%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmnet
%global packver   4.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Lasso and Elastic-Net Regularized Generalized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Matrix >= 1.0.6
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix >= 1.0.6
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rcpp 

%description
Extremely efficient procedures for fitting the entire lasso or elastic-net
regularization path for linear regression, logistic and multinomial
regression models, Poisson regression, Cox model, multiple-response
Gaussian, and the grouped multinomial regression. There are two new and
important additions. The family argument can be a GLM family object, which
opens the door to any programmed family. This comes with a modest
computational cost, so when the built-in families suffice, they should be
used instead.  The other novelty is the relax option, which refits each of
the active sets in the path unpenalized. The algorithm uses cyclical
coordinate descent in a path-wise fashion, as described in the papers
listed in the URL below.

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
