%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mase
%global packver   0.1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Assisted Survey Estimators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rpms 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rpms 
Requires:         R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-Rcpp 

%description
A set of model-assisted survey estimators and corresponding variance
estimators for single stage, unequal probability, without replacement
sampling designs.  All of the estimators can be written as a generalized
regression estimator with the Horvitz-Thompson, ratio, post-stratified,
and regression estimators summarized by Sarndal et al. (1992,
ISBN:978-0-387-40620-6). Two of the estimators employ a statistical
learning model as the assisting model: the elastic net regression
estimator, which is an extension of the lasso regression estimator given
by McConville et al. (2017) <doi:10.1093/jssam/smw041>, and the regression
tree estimator described in McConville and Toth (2017) <arXiv:1712.05708>.
The variance estimators which approximate the joint inclusion
probabilities can be found in Berger and Tille (2009)
<doi:10.1016/S0169-7161(08)00002-3> and the bootstrap variance estimator
is presented in Mashreghi et al. (2016) <doi:10.1214/16-SS113>.

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
