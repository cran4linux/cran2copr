%global __brp_check_rpaths %{nil}
%global packname  IntegratedMRF
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Integrated Prediction using Uni-Variate and Multivariate RandomForests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-bootstrap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-MultivariateRandomForest 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-bootstrap 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-MultivariateRandomForest 

%description
An implementation of a framework for drug sensitivity prediction from
various genetic characterizations using ensemble approaches. Random
Forests or Multivariate Random Forest predictive models can be generated
from each genetic characterization that are then combined using a Least
Square Regression approach. It also provides options for the use of
different error estimation approaches of Leave-one-out, Bootstrap, N-fold
cross validation and 0.632+Bootstrap along with generation of prediction
confidence interval using Jackknife-after-Bootstrap approach.

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
