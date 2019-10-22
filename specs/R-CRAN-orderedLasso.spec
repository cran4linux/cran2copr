%global debug_package %{nil}
%global packname  orderedLasso
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}
Summary:          Ordered Lasso and Time-Lag Sparse Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-Matrix 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Ordered lasso and time-lag sparse regression. Ordered Lasso fits a linear
model and imposes an order constraint on the coefficients. It writes the
coefficients as positive and negative parts, and requires positive parts
and negative parts are non-increasing and positive. Time-Lag Lasso
generalizes the ordered Lasso to a general data matrix with multiple
predictors. For more details, see Suo, X.,Tibshirani, R., (2014) 'An
Ordered Lasso and Sparse Time-lagged Regression'.

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
