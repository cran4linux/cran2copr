%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastcpd
%global packver   0.13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Change Point Detection via Sequential Gradient Descent

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-fastglm 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-fastglm 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-tseries 
Requires:         R-utils 

%description
Implements fast change point detection algorithm based on the paper
"Sequential Gradient Descent and Quasi-Newton's Method for Change-Point
Analysis" by Xianyang Zhang, Trisha Dawn
<https://proceedings.mlr.press/v206/zhang23b.html>. The algorithm is based
on dynamic programming with pruning and sequential gradient descent. It is
able to detect change points a magnitude faster than the vanilla Pruned
Exact Linear Time(PELT). The package includes examples of linear
regression, logistic regression, Poisson regression, penalized linear
regression data, and whole lot more examples with custom cost function in
case the user wants to use their own cost function.

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
