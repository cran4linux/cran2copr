%global __brp_check_rpaths %{nil}
%global packname  RSDA
%global packver   3.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          R to Symbolic Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-vctrs >= 0.2.4
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpolypath 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-princurve 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-tsne 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-vctrs >= 0.2.4
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 
Requires:         R-stats 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpolypath 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-princurve 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-tsne 

%description
Symbolic Data Analysis (SDA) was proposed by professor Edwin Diday in
1987, the main purpose of SDA is to substitute the set of rows (cases) in
the data table for a concept (second order statistical unit). This package
implements, to the symbolic case, certain techniques of automatic
classification, as well as some linear models.

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
