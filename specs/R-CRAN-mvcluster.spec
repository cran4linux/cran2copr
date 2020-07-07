%global packname  mvcluster
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Multi-View Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.0

%description
Implementation of multi-view bi-clustering algorithms. When a sample is
characterized by two or more sets of input features, it creates multiple
data matrices for the same set of examples, each corresponding to a view.
For instance, individuals who are diagnosed with a disorder can be
described by their clinical symptoms (one view) and their genomic markers
(another view). Rows of a data matrix correspond to examples and columns
correspond to features. A multi-view bi-clustering algorithm groups
examples (rows) consistently across the views and simultaneously
identifies the subset of features (columns) in each view that are
associated with the row groups. This mvcluster package includes three such
methods. (1) MVSVDL1: multi-view bi-clustering based on singular value
decomposition where the left singular vectors are used to identify row
clusters and the right singular vectors are used to identify features
(columns) for each row cluster. Each singular vector is regularized by the
L1 vector norm.  (2) MVLRRL0: multi-view bi-clustering based on sparse low
rank representation (i.e., matrix approximation) where the decomposed
components are regularized by the so-called L0 vector norm (which is not
really a vector norm). (3) MVLRRL1: multi-view bi-clustering based on
sparse low rank representation (i.e., matrix approximation) where the
decomposed components are regularized by the L1 vector norm.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
