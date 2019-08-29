%global packname  kexpmv
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Matrix Exponential using Krylov Subspace Routines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-CRAN-SparseM 

%description
Implements functions from 'EXPOKIT'
(<https://www.maths.uq.edu.au/expokit/>) to calculate matrix exponentials,
Sidje RB, (1998) <doi:10.1145/285861.285868>. Includes functions for small
dense matrices along with functions for large sparse matrices. The
functions for large sparse matrices implement Krylov subspace methods
which help minimise the computational complexity for matrix exponentials.
'Kexpmv' can be utilised to calculate both the matrix exponential in
isolation along with the product of the matrix exponential and a vector.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/notes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
