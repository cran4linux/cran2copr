%global packname  CMLS
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Constrained Multivariate Least Squares

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-parallel 
Requires:         R-CRAN-quadprog 
Requires:         R-parallel 

%description
Solves multivariate least squares (MLS) problems subject to constraints on
the coefficients, e.g., non-negativity, orthogonality, equality,
inequality, monotonicity, unimodality, smoothness, etc. Includes flexible
functions for solving MLS problems subject to user-specified equality
and/or inequality constraints, as well as a wrapper function that
implements 24 common constraint options. Also does k-fold or generalized
cross-validation to tune constraint options for MLS problems. See ten
Berge (1993, ISBN:9789066950832) for an overview of MLS problems, and see
Goldfarb and Idnani (1983) <doi:10.1007/BF02591962> for a discussion of
the underlying quadratic programming algorithm.

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
