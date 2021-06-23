%global __brp_check_rpaths %{nil}
%global packname  RSpectra
%global packver   0.16-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          3%{?dist}%{?buildtag}
Summary:          Solvers for Large-Scale Eigenvalue and SVD Problems

License:          MPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-Matrix >= 1.1.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
Requires:         R-Matrix >= 1.1.0
Requires:         R-CRAN-Rcpp >= 0.11.5

%description
R interface to the 'Spectra' library <https://spectralib.org/> for
large-scale eigenvalue and SVD problems. It is typically used to compute a
few eigenvalues/vectors of an n by n matrix, e.g., the k largest
eigenvalues, which is usually more efficient than eigen() if k << n. This
package provides the 'eigs()' function that does the similar job as in
'Matlab', 'Octave', 'Python SciPy' and 'Julia'. It also provides the
'svds()' function to calculate the largest k singular values and
corresponding singular vectors of a real matrix. The matrix to be computed
on can be dense, sparse, or in the form of an operator defined by the
user.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
