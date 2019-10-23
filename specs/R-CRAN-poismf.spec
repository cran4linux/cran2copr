%global packname  poismf
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Factorization of Sparse Counts Matrices Through PoissonLikelihood

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nonneg.cg 
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-CRAN-nonneg.cg 

%description
Creates a low-rank factorization of a sparse counts matrix by maximizing
Poisson likelihood with l1/l2 regularization with all non-negative latent
factors (e.g. for recommender systems or topic modeling) (Cortes, David,
2018, <arXiv:1811.01908>). Similar to hierarchical Poisson factorization,
but follows an optimization-based approach with regularization instead of
a hierarchical structure, and is fit through either proximal gradient or
conjugate gradient instead of variational inference.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
