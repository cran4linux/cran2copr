%global __brp_check_rpaths %{nil}
%global packname  MLModelSelection
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Model Selection in Multivariate Longitudinal Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-MASS 

%description
An efficient Gibbs sampling algorithm is developed for Bayesian
multivariate longitudinal data analysis with the focus on selection of
important elements in the generalized autoregressive matrix. It provides
posterior samples and estimates of parameters. In addition, estimates of
several information criteria such as Akaike information criterion (AIC),
Bayesian information criterion (BIC), deviance information criterion (DIC)
and prediction accuracy such as the marginal predictive likelihood (MPL)
and the mean squared prediction error (MSPE) are provided for model
selection.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
