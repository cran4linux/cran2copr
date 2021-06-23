%global __brp_check_rpaths %{nil}
%global packname  llbayesireg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          The L-Logistic Bayesian Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-llogistic 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
Requires:         R-CRAN-StanHeaders >= 2.18.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-llogistic 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-MCMCpack 
Requires:         R-MASS 
Requires:         R-CRAN-coda 
Requires:         R-stats 

%description
R functions and data sets for the work Paz, R.F., Balakrishnan, N and
Bazán, J.L. (2018). L-logistic regression models: Prior sensitivity
analysis, robustness to outliers and applications. Brazilian Journal of
Probability and Statistics,
<https://www.imstat.org/wp-content/uploads/2018/05/BJPS397.pdf>.

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
