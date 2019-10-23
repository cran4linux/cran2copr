%global packname  catSurv
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Computerized Adaptive Testing for Survey Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-BH >= 1.62.0.1
BuildRequires:    R-CRAN-ltm >= 1.0.0
BuildRequires:    R-CRAN-RcppGSL >= 0.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ltm >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-RcppParallel 

%description
Provides methods of computerized adaptive testing for survey researchers.
Includes functionality for data fit with the classic item response methods
including the latent trait model, Birnbaum`s three parameter model, the
graded response, and the generalized partial credit model.  Additionally,
includes several ability parameter estimation and item selection routines.
During item selection, all calculations are done in compiled C++ code.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
