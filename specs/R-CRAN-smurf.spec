%global packname  smurf
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Sparse Multi-Type Regularized Feature Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.300.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-catdata 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-mgcv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-catdata 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-mgcv 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-speedglm 
Requires:         R-stats 

%description
Implementation of the SMuRF algorithm of Devriendt et al. (2018)
<arXiv:1810.03136> to fit generalized linear models (GLMs) with multiple
types of predictors via regularized maximum likelihood.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
