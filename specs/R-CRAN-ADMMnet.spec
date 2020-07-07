%global packname  ADMMnet
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Regularized Model with Selecting the Number of Non-Zeros

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.2.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix >= 1.2.3
Requires:         R-CRAN-Rcpp >= 0.12.2

%description
Fit linear and cox models regularized with net (L1 and Laplacian),
elastic-net (L1 and L2) or lasso (L1) penalty, and their adaptive forms,
such as adaptive lasso and net adjusting for signs of linked coefficients.
In addition, it treats the number of non-zero coefficients as another
tuning parameter and simultaneously selects with the regularization
parameter. The package uses one-step coordinate descent algorithm and runs
extremely fast by taking into account the sparsity structure of
coefficients.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
