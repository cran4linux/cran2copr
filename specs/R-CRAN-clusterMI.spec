%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clusterMI
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Analysis with Missing Values by Multiple Imputation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-micemd 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mix 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-knockoff 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-diceR 
BuildRequires:    R-CRAN-NPBayesImputeCat 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-cat 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-micemd 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mix 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-knockoff 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-diceR 
Requires:         R-CRAN-NPBayesImputeCat 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-cat 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Allows clustering of incomplete observations by addressing missing values
using multiple imputation. For achieving this goal, the methodology
consists in three steps, following Audigier and Niang 2022
<doi:10.1007/s11634-022-00519-1>. I) Missing data imputation using
dedicated models. Four multiple imputation methods are proposed, two are
based on joint modelling and two are fully sequential methods, as
discussed in Audigier et al. (2021) <doi:10.48550/arXiv.2106.04424>. II)
cluster analysis of imputed data sets. Six clustering methods are
available (distances-based or model-based), but custom methods can also be
easily used. III) Partition pooling. The set of partitions is aggregated
using Non-negative Matrix Factorization based method. An associated
instability measure is computed by bootstrap (see Fang, Y. and Wang, J.,
2012 <doi:10.1016/j.csda.2011.09.003>). Among applications, this
instability measure can be used to choose a number of clusters with
missing values. The package also proposes several diagnostic tools to tune
the number of imputed data sets, to tune the number of iterations in fully
sequential imputation, to check the fit of imputation models, etc.

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
