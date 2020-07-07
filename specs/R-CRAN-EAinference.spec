%global packname  EAinference
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Estimator Augmentation and Simulation-Based Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-hdi 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-limSolve 
Requires:         R-MASS 
Requires:         R-CRAN-hdi 
Requires:         R-CRAN-Rcpp 

%description
Estimator augmentation methods for statistical inference on
high-dimensional data, as described in Zhou, Q. (2014) <arXiv:1401.4425v2>
and Zhou, Q. and Min, S. (2017) <doi:10.1214/17-EJS1309>. It provides
several simulation-based inference methods: (a) Gaussian and wild
multiplier bootstrap for lasso, group lasso, scaled lasso, scaled group
lasso and their de-biased estimators, (b) importance sampler for
approximating p-values in these methods, (c) Markov chain Monte Carlo
lasso sampler with applications in post-selection inference.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
