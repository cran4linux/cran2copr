%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MBMethPred
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Medulloblastoma Subgroups Prediction

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-SNFtool 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-SNFtool 
Requires:         R-CRAN-class 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-xgboost 

%description
Utilizing a combination of machine learning models (Random Forest, Naive
Bayes, K-Nearest Neighbor, Support Vector Machines, Extreme Gradient
Boosting, and Linear Discriminant Analysis) and a deep Artificial Neural
Network model, 'MBMethPred' can predict medulloblastoma subgroups,
including wingless (WNT), sonic hedgehog (SHH), Group 3, and Group 4 from
methylation data.

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
