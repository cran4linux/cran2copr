%global packname  KoulMde
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          Koul's Minimum Distance Estimation in Linear Regression andAutoregression Model by Coordinate Descent Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-expm 

%description
Consider linear regression model and autoregressive model of order q where
errors in the linear regression model and innovations in the
autoregression model are independent and symmetrically distributed. Hira
L. Koul (1986) <DOI:10.1214/aos/1176350059> proposed a nonparametric
minimum distance estimation method by minimizing L2-type distance between
certain weighted residual empirical processes. He also proposed a simpler
version of the loss function by using symmetry of the integrating measure
in the distance. Kim (2018) <DOI:10.1080/00949655.2017.1392527> proposed a
fast computational method which enables practitioners to compute the
minimum distance estimator of the vector of general multiple regression
parameters for several integrating measures. This package contains three
functions: KoulLrMde(), KoulArMde(), and Koul2StageMde(). The former two
provide minimum distance estimators for linear regression model and
autoregression model, respectively, where both are based on Koul's method.
These two functions take much less time for the computation than those
based on parametric minimum distance estimation methods. Koul2StageMde()
provides estimators for regression and autoregressive coefficients of
linear regression model with autoregressive errors through minimum distant
method of two stages. The new version is written in Rcpp and dramatically
reduces computational time.

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
