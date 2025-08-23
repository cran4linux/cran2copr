%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robCompositions
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-robustHD 
BuildRequires:    R-CRAN-sparsepca 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-CRAN-zCompositions 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-robustHD 
Requires:         R-CRAN-sparsepca 
Requires:         R-splines 
Requires:         R-CRAN-VIM 
Requires:         R-CRAN-zCompositions 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rcpp 

%description
Methods for analysis of compositional data including robust methods
(<doi:10.1007/978-3-319-96422-5>), imputation of missing values
(<doi:10.1016/j.csda.2009.11.023>), methods to replace rounded zeros
(<doi:10.1080/02664763.2017.1410524>,
<doi:10.1016/j.chemolab.2016.04.011>, <doi:10.1016/j.csda.2012.02.012>),
count zeros (<doi:10.1177/1471082X14535524>), methods to deal with
essential zeros (<doi:10.1080/02664763.2016.1182135>), (robust) outlier
detection for compositional data, (robust) principal component analysis
for compositional data, (robust) factor analysis for compositional data,
(robust) discriminant analysis for compositional data (Fisher rule),
robust regression with compositional predictors, functional data analysis
(<doi:10.1016/j.csda.2015.07.007>) and p-splines
(<doi:10.1016/j.csda.2015.07.007>), contingency
(<doi:10.1080/03610926.2013.824980>) and compositional tables
(<doi:10.1111/sjos.12326>, <doi:10.1111/sjos.12223>,
<doi:10.1080/02664763.2013.856871>) and (robust) Anderson-Darling
normality tests for compositional data as well as popular log-ratio
transformations (addLR, cenLR, isomLR, and their inverse transformations).
In addition, visualisation and diagnostic tools are implemented as well as
high and low-level plot functions for the ternary diagram.

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
