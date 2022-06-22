%global __brp_check_rpaths %{nil}
%global packname  randomUniformForest
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Random Uniform Forests for Classification, Regression and Unsupervised Learning

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-foreach >= 1.4.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-foreach >= 1.4.2
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-MASS 

%description
Ensemble model, for classification, regression and unsupervised learning,
based on a forest of unpruned and randomized binary decision trees. Each
tree is grown by sampling, with replacement, a set of variables at each
node. Each cut-point is generated randomly, according to the continuous
Uniform distribution. For each tree, data are either bootstrapped or
subsampled. The unsupervised mode introduces clustering, dimension
reduction and variable importance, using a three-layer engine. Random
Uniform Forests are mainly aimed to lower correlation between trees (or
trees residuals), to provide a deep analysis of variable importance and to
allow native distributed and incremental learning.

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
