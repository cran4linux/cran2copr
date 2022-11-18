%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClusROC
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          ROC Analysis in Three-Class Classification Problems for Clustered Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Statistical methods for ROC surface analysis in three-class classification
problems for clustered data and in presence of covariates. In particular,
the package allows to obtain covariate-specific point and interval
estimation for: (i) true class fractions (TCFs) at fixed pairs of
thresholds; (ii) the ROC surface; (iii) the volume under ROC surface
(VUS); (iv) the optimal pairs of thresholds. Methods considered in points
(i), (ii) and (iv) are proposed and discussed in To et al. (2022)
<doi:10.1177/09622802221089029>. Referring to point (iv), three different
selection criteria are implemented: Generalized Youden Index (GYI),
Closest to Perfection (CtP) and Maximum Volume (MV). Methods considered in
point (iii) are proposed and discussed in Xiong et al. (2018)
<doi:10.1177/0962280217742539>. Visualization tools are also provided. We
refer readers to the articles cited above for all details.

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
