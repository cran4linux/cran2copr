%global packname  kernDeepStackNet
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Kernel Deep Stacking Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-DiceOptim 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-globalOptTests 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-DiceOptim 
Requires:         R-CRAN-DiceKriging 
Requires:         R-parallel 
Requires:         R-CRAN-globalOptTests 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-caret 

%description
Contains functions for estimation and model selection of kernel deep
stacking networks.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
