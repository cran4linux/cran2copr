%global packname  rpf
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Response Probability Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lifecycle 

%description
The purpose of this package is to factor out logic and math common to Item
Factor Analysis fitting, diagnostics, and analysis. It is envisioned as
core support code suitable for more specialized IRT packages to build
upon. Complete access to optimized C functions are made available with
R_RegisterCCallable().

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
