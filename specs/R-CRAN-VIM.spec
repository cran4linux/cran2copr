%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VIM
%global packver   7.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization and Imputation of Missing Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-mlr3tuning 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-future 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-colorspace 
Requires:         R-grid 
Requires:         R-CRAN-car 
Requires:         R-grDevices 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-mlr3tuning 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-future 

%description
Provides methods for imputation and visualization of missing values. It
includes graphical tools to explore the amount, structure and patterns of
missing and/or imputed values, supporting exploratory data analysis and
helping to investigate potential missingness mechanisms (details in
Alfons, Templ and Filzmoser, <doi:10.1007/s11634-011-0102-y>. The quality
of imputations can be assessed visually using a wide range of univariate,
bivariate and multivariate plots. The package further provides several
imputation methods, including efficient implementations of k-nearest
neighbour and hot-deck imputation (Kowarik and Templ 2013,
<doi:10.18637/jss.v074.i07>, iterative robust model-based multiple
imputation (Templ 2011, <doi:10.1016/j.csda.2011.04.012>; Templ 2023,
<doi:10.3390/math11122729>), and machine learning–based approaches such as
robust GAM-based multiple imputation (Templ 2024,
<doi:10.1007/s11222-024-10429-1>) as well as gradient boosting (XGBoost)
and transformer-based methods (Niederhametner et al.,
<doi:10.1177/18747655251339401>). General background and practical
guidance on imputation are provided in the Springer book by Templ (2023)
<doi:10.1007/978-3-031-30073-8>.

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
