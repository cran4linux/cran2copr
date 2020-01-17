%global packname  uwot
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          The Uniform Manifold Approximation and Projection (UMAP) Methodfor Dimensionality Reduction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppAnnoy >= 0.0.11
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-dqrng 
Requires:         R-CRAN-RcppAnnoy >= 0.0.11
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-irlba 

%description
An implementation of the Uniform Manifold Approximation and Projection
dimensionality reduction by McInnes et al. (2018) <arXiv:1802.03426>. It
also provides means to transform new data and to carry out supervised
dimensionality reduction. An implementation of the related LargeVis method
of Tang et al. (2016) <arXiv:1602.00370> is also provided. This is a
complete re-implementation in R (and C++, via the 'Rcpp' package): no
Python installation is required. See the uwot website
(<https://github.com/jlmelville/uwot>) for more documentation and
examples.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
