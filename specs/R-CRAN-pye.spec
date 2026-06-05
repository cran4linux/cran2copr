%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pye
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Youden Index Estimator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-evmix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-OptimalCutpoints 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-penalizedSVM 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ROCnReg 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-sparseSVM 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-evmix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-OptimalCutpoints 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-penalizedSVM 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ROCnReg 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-sparseSVM 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Implements the Penalized Youden Index Estimator (PYE) and the
Covariate-Adjusted Youden Index Estimator (covYI), providing a novel
framework for feature and covariate selection and combination in
high-dimensional binary classification problems. Methodologies are based
on Salaroli and Pardo (2023) <doi:10.1016/j.chemolab.2023.104786> and an
unpublished manuscript by Salaroli and Pardo (2026) under review.

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
