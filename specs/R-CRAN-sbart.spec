%global packname  sbart
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Sequential BART for Imputation of Missing Covariates

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-Rcpp 

%description
Implements the sequential BART (Bayesian Additive Regression Trees)
approach to impute the missing covariates. The algorithm applies a
Bayesian nonparametric approach on factored sets of sequential
conditionals of the joint distribution of the covariates and the
missingness and applying the Bayesian additive regression trees to model
each of these univariate conditionals. Each conditional distribution is
then sampled using MCMC algorithm. The published journal can be found at
<https://doi.org/10.1093/biostatistics/kxw009> Package provides a
function, seqBART(), which computes and returns the imputed values.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
