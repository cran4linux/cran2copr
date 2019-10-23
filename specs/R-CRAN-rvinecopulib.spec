%global packname  rvinecopulib
%global packver   0.3.2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2.1.1
Release:          1%{?dist}
Summary:          High Performance Algorithms for Vine Copula Modeling

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cctools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-kde1d 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-wdm 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cctools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-kde1d 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an interface to 'vinecopulib', a C++ library for vine copula
modeling based on 'Boost' and 'Eigen'. The 'rvinecopulib' package
implements the core features of the popular 'VineCopula' package, in
particular inference algorithms for both vine copula and bivariate copula
models. Advantages over 'VineCopula' are a sleeker and more modern API,
improved performances, especially in high dimensions, nonparametric and
multi-parameter families. The 'rvinecopulib' package includes
'vinecopulib' as header-only C++ library (currently version 0.3.1). Thus
users do not need to install 'vinecopulib' itself in order to use
'rvinecopulib'. Since their initial releases, 'vinecopulib' is licensed
under the MIT License, and 'rvinecopulib' is licensed under the GNU GPL
version 3.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
