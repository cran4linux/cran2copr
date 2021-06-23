%global __brp_check_rpaths %{nil}
%global packname  cblasr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          The C Interface to 'BLAS' Routines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Provides the 'cblas.h' header file as C interface to the underlying
internal 'BLAS' library in R. 'CBLAS'
<https://www.netlib.org/blas/cblas.h> is a collection of wrappers
originally written by Keita Teranishi and provides a C interface to the
FORTRAN 'BLAS' library <https://www.netlib.org/blas/>. Note that as
internal 'BLAS' library provided by R
<https://svn.r-project.org/R/trunk/src/include/R_ext/BLAS.h> is used and
only the double precision / double complex 'BLAS' routines are supported.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
