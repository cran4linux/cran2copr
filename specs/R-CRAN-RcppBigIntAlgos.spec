%global packname  RcppBigIntAlgos
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          2%{?dist}
Summary:          Factor Big Integers with the Quadratic Sieve

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel >= 4.2.3
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-Rcpp 

%description
Features the multiple polynomial quadratic sieve (MPQS) algorithm for
factoring large integers and a vectorized factoring function that returns
the complete factorization of an integer. The MPQS is based off of the
seminal work of Carl Pomerance (1984) <doi:10.1007/3-540-39757-4_17> along
with the modification of multiple polynomials introduced by Peter
Montgomery and J. Davis as outlined by Robert D. Silverman (1987)
<doi:10.1090/S0025-5718-1987-0866119-8>. Utilizes the C library GMP (GNU
Multiple Precision Arithmetic). The Pollard's rho algorithm for factoring
smaller numbers is the same algorithm used by the factorize function in
the 'gmp' package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
