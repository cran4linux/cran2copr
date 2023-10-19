%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  misspi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Missing Value Imputation in Parallel

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-SIS 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-SIS 
Requires:         R-CRAN-plotly 

%description
A framework that boosts the imputation of 'missForest' by Stekhoven, D.J.
and Bühlmann, P. (2012) <doi:10.1093/bioinformatics/btr597> by harnessing
parallel processing and through the fast Gradient Boosted Decision Trees
(GBDT) implementation 'LightGBM' by Ke, Guolin et al.(2017)
<https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision>.
'misspi' has the following main advantages: 1. Allows embrassingly
parallel imputation on large scale data. 2. Accepts a variety of machine
learning models as methods with friendly user portal. 3. Supports multiple
initializations methods. 4. Supports early stopping that prohibits
unnecessary iterations.

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
