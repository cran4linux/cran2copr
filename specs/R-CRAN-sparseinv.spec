%global __brp_check_rpaths %{nil}
%global packname  sparseinv
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Computation of the Sparse Inverse Subset

License:          GPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spam 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spam 

%description
Creates a wrapper for the 'SuiteSparse' routines that execute the
Takahashi equations. These equations compute the elements of the inverse
of a sparse matrix at locations where the its Cholesky factor is
structurally non-zero. The resulting matrix is known as a sparse inverse
subset. Some helper functions are also implemented. Support for spam
matrices is currently limited and will be implemented in the future. See
Rue and Martino (2007) <doi:10.1016/j.jspi.2006.07.016> and Zammit-Mangion
and Rougier (2018) <doi:10.1016/j.csda.2018.02.001> for the application of
these equations to statistics.

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
