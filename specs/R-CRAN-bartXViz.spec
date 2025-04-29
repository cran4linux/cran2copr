%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bartXViz
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of BART and BARP using SHAP

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-bartMachine 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggfittext 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gggenes 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-dbarts 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-bartMachine 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggfittext 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gggenes 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-abind 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-dbarts 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-missForest 

%description
The contribution of variables in Bayesian Additive Regression Trees (BART)
and Bayesian Additive Regression Trees with Post-Stratification (BARP)
models is computed using permutation-based Shapley values. The computed
SHAP values are then utilized to visualize the contribution of each
variable through various plots. The computation of SHAP values for most
models follows the methodology proposed by Strumbel and Kononenko (2014)
<doi:10.1007/s10115-013-0679-x>, while for XGBoost, the approach
introduced by Lundberg et al. (2020) <doi:10.1038/s42256-019-0138-9> was
also considered. The BART model was referenced based on the works of
Chipman, George, and McCulloch (2010) <doi:10.1214/09-AOAS285> and
Kapelner and Bleich (2013) <doi:10.18637/jss.v070.i04>, while the
methodology for the BARP model was based on Bisbee (2019)
<doi:10.1017/S0003055419000480>.

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
