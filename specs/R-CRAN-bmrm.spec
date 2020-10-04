%global packname  bmrm
%global packver   4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bundle Methods for Regularized Risk Minimization Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-LowRankQP 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-LowRankQP 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Rcpp 

%description
Bundle methods for minimization of convex and non-convex risk under L1 or
L2 regularization. Implements the algorithm proposed by Teo et al. (JMLR
2010) as well as the extension proposed by Do and Artieres (JMLR 2012).
The package comes with lot of loss functions for machine learning which
make it powerful for big data analysis. The applications includes:
structured prediction, linear SVM, multi-class SVM, f-beta optimization,
ROC optimization, ordinal regression, quantile regression, epsilon
insensitive regression, least mean square, logistic regression, least
absolute deviation regression (see package examples), etc... all with L1
and L2 regularization.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
