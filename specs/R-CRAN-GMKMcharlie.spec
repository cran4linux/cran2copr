%global packname  GMKMcharlie
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Unsupervised Gaussian Mixture and Minkowski K-Means

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-RcppParallel 

%description
High performance trainers for parameterizing and clustering weighted data.
The Gaussian mixture (GM) module includes the conventional EM (expectation
maximization) trainer, the component-wise EM trainer, the
minimum-message-length EM trainer by Figueiredo and Jain (2002)
<doi:10.1109/34.990138>. These trainers accept additional constraints on
mixture weights and covariance eigen ratios. The K-means (KM) module
offers clustering with the options of (i) deterministic and stochastic
K-means++ initializations, (ii) upper bounds on cluster weights (sizes),
(iii) Minkowski distances, (iv) cosine dissimilarity, (v) dense and sparse
representation of data input. The package improved the usual
implementations of GM and KM training algorithms in various aspects. It is
carefully crafted in multithreaded C++ for processing large data in
industry use.

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
