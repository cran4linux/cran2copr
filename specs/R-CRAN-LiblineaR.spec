%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LiblineaR
%global packver   2.10-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.22
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Predictive Models Based on the LIBLINEAR C/C++ Library

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
A wrapper around the LIBLINEAR C/C++ library for machine learning
(available at <https://www.csie.ntu.edu.tw/~cjlin/liblinear/>). LIBLINEAR
is a simple library for solving large-scale regularized linear
classification and regression. It currently supports L2-regularized
classification (such as logistic regression, L2-loss linear SVM and
L1-loss linear SVM) as well as L1-regularized classification (such as
L2-loss linear SVM and logistic regression) and L2-regularized support
vector regression (with L1- or L2-loss). The main features of LiblineaR
include multi-class classification (one-vs-the rest, and Crammer & Singer
method), cross validation for model selection, probability estimates
(logistic regression only) or weights for unbalanced data. The estimation
of the models is particularly fast as compared to other libraries.

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
