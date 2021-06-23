%global __brp_check_rpaths %{nil}
%global packname  sparsereg
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Sparse Bayesian Models for Regression, Subgroup Analysis, andPanel Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-GIGrvg 

%description
Sparse modeling provides a mean selecting a small number of non-zero
effects from a large possible number of candidate effects.  This package
includes a suite of methods for sparse modeling: estimation via EM or
MCMC, approximate confidence intervals with nominal coverage, and
diagnostic and summary plots.  The method can implement sparse linear
regression and sparse probit regression.  Beyond regression analyses,
applications include subgroup analysis, particularly for conjoint
experiments, and panel data. Future versions will include extensions to
models with truncated outcomes, propensity score, and instrumental
variable analysis.

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
