%global packname  treenomial
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Comparison of Trees using a Tree Defining Polynomial

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-ape 
Requires:         R-methods 

%description
Provides functionality for creation and comparison of polynomials that
uniquely describe trees as introduced in Liu (2019, <arXiv:1904.03332>).
The core method converts rooted unlabeled phylo objects from 'ape' to the
tree defining polynomials described with coefficient matrices.
Additionally, a conversion for rooted binary trees with binary trait
labels is also provided. Once the polynomials of trees are calculated
there are functions to calculate distances, distance matrices and plot
different distance trees from a target tree. Manipulation and conversion
to the tree defining polynomials is implemented in C++ with 'Rcpp' and
'RcppArmadillo'. Furthermore, parallel programming with 'RcppThread' is
used to improve performance converting to polynomials and calculating
distances.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
