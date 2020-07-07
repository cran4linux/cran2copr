%global packname  RMKL
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Multiple Kernel Learning for Classification or RegressionProblems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-caret 
Requires:         R-CRAN-kernlab 
Requires:         R-stats 
Requires:         R-CRAN-e1071 

%description
Provides R and C++ function that enable the user to conduct multiple
kernel learning (MKL) and cross validation for support vector machine
(SVM) models. Cross validation can be used to identify kernel shapes and
hyperparameter combinations that can be used as candidate kernels for MKL.
There are three implementations provided in this package, namely SimpleMKL
Alain Rakotomamonjy et. al (2008), Simple and Efficient MKL Xu et. al
(2010), and Dual augmented Lagrangian MKL Suzuki and Tomioka (2011)
<doi:10.1007/s10994-011-5252-9>. These methods identify the convex
combination of candidate kernels to construct an optimal hyperplane.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
