%global __brp_check_rpaths %{nil}
%global packname  dmlalg
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Double Machine Learning Algorithms

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 
Requires:         R-splines 
Requires:         R-CRAN-randomForest 

%description
Implementation of double machine learning (DML) algorithms in R, based on
Emmenegger and Buehlmann (2021) "Regularizing Double Machine Learning in
Partially Linear Endogenous Models" <arXiv:2101.12525> and Emmenegger and
Buehlmann (2021) <arXiv:2108.13657> "Double Machine Learning for Partially
Linear Mixed-Effects Models with Repeated Measurements". First part: our
goal is to perform inference for the linear parameter in partially linear
models with confounding variables. The standard DML estimator of the
linear parameter has a two-stage least squares interpretation, which can
lead to a large variance and overwide confidence intervals. We apply
regularization to reduce the variance of the estimator, which produces
narrower confidence intervals that are approximately valid. Nuisance terms
can be flexibly estimated with machine learning algorithms. Second part:
our goal is to estimate and perform inference for the linear coefficient
in a partially linear mixed-effects model with DML. Machine learning
algorithms allows us to incorporate more complex interaction structures
and high-dimensional variables.

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
