%global packname  LiblineaR
%global packver   2.10-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.8
Release:          3%{?dist}
Summary:          Linear Predictive Models Based on the 'LIBLINEAR' C/C++ Library

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
A wrapper around the 'LIBLINEAR' C/C++ library for machine learning
(available at <http://www.csie.ntu.edu.tw/~cjlin/liblinear>). 'LIBLINEAR'
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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
