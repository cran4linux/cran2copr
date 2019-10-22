%global packname  sparseEigen
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Computation of Sparse Eigenvectors of a Matrix

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch

%description
Computation of sparse eigenvectors of a matrix (aka sparse PCA) with
running time 2-3 orders of magnitude lower than existing methods and
better final performance in terms of recovery of sparsity pattern and
estimation of numerical values. Can handle covariance matrices as well as
data matrices with real or complex-valued entries. Different levels of
sparsity can be specified for each individual ordered eigenvector and the
method is robust in parameter selection. See vignette for a detailed
documentation and comparison, with several illustrative examples. The
package is based on the paper: K. Benidis, Y. Sun, P. Babu, and D. P.
Palomar (2016). "Orthogonal Sparse PCA and Covariance Estimation via
Procrustes Reformulation," IEEE Transactions on Signal Processing
<doi:10.1109/TSP.2016.2605073>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
