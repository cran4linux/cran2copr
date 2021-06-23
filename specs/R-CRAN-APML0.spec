%global __brp_check_rpaths %{nil}
%global packname  APML0
%global packver   0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10
Release:          3%{?dist}%{?buildtag}
Summary:          Augmented and Penalized Minimization Method L0

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix >= 1.2.10
Requires:         R-CRAN-Rcpp >= 0.12.12

%description
Fit linear, logistic and Cox models regularized with L0, lasso (L1),
elastic-net (L1 and L2), or net (L1 and Laplacian) penalty, and their
adaptive forms, such as adaptive lasso / elastic-net and net adjusting for
signs of linked coefficients. It solves L0 penalty problem by
simultaneously selecting regularization parameters and performing
hard-thresholding or selecting number of non-zeros. This augmented and
penalized minimization method provides an approximation solution to the L0
penalty problem, but runs as fast as L1 regularization problem. The
package uses one-step coordinate descent algorithm and runs extremely fast
by taking into account the sparsity structure of coefficients. It could
deal with very high dimensional data and has superior selection
performance.

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
