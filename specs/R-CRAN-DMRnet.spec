%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DMRnet
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Delete or Merge Regressors Algorithms for Linear and Logistic Model Selection and High-Dimensional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grpreg 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Model selection algorithms for regression and classification, where the
predictors can be continuous or categorical and the number of regressors
may exceed the number of observations. The selected model consists of a
subset of numerical regressors and partitions of levels of factors.
Aleksandra Maj-Kańska, Piotr Pokarowski and Agnieszka Prochenka, 2015.
Delete or merge regressors for linear model selection. Electronic Journal
of Statistics 9(2): 1749-1778. <doi:10.1214/15-EJS1050>. Piotr Pokarowski
and Jan Mielniczuk, 2015. Combined l1 and greedy l0 penalized least
squares for linear model selection. Journal of Machine Learning Research
16(29): 961-992.
<https://www.jmlr.org/papers/volume16/pokarowski15a/pokarowski15a.pdf>.
Piotr Pokarowski, Wojciech Rejchel, Agnieszka Sołtys, Michał Frej and Jan
Mielniczuk, 2022. Improving Lasso for model selection and prediction.
Scandinavian Journal of Statistics, 49(2): 831–863.
<doi:10.1111/sjos.12546>.

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
