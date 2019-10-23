%global packname  mirtjml
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Joint Maximum Likelihood Estimation for High-Dimensional ItemFactor Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-stats 
Requires:         R-CRAN-GPArotation 

%description
Provides constrained joint maximum likelihood estimation algorithms for
item factor analysis (IFA) based on multidimensional item response theory
models. So far, we provide functions for exploratory and confirmatory IFA
based on the multidimensional two parameter logistic (M2PL) model for
binary response data. Comparing with traditional estimation methods for
IFA, the methods implemented in this package scale better to data with
large numbers of respondents, items, and latent factors. The computation
is facilitated by multiprocessing 'OpenMP' API. For more information,
please refer to: 1. Chen, Y., Li, X., & Zhang, S. (2018). Joint Maximum
Likelihood Estimation for High-Dimensional Exploratory Item Factor
Analysis. Psychometrika, 1-23. <doi:10.1007/s11336-018-9646-5>; 2. Chen,
Y., Li, X., & Zhang, S. (2017). Structured Latent Factor Analysis for
Large-scale Data: Identifiability, Estimability, and Their Implications.
arXiv preprint <arXiv:1712.08966>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
