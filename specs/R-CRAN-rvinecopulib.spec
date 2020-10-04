%global packname  rvinecopulib
%global packver   0.5.4.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Performance Algorithms for Vine Copula Modeling

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-kde1d >= 1.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-wdm 
Requires:         R-CRAN-kde1d >= 1.0.2
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-assertthat 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an interface to 'vinecopulib', a C++ library for vine copula
modeling. The 'rvinecopulib' package implements the core features of the
popular 'VineCopula' package, in particular inference algorithms for both
vine copula and bivariate copula models. Advantages over 'VineCopula' are
a sleeker and more modern API, improved performances, especially in high
dimensions, nonparametric and multi-parameter families, and the ability to
model discrete variables. The 'rvinecopulib' package includes
'vinecopulib' as header-only C++ library (currently version 0.5.4). Thus
users do not need to install 'vinecopulib' itself in order to use
'rvinecopulib'. Since their initial releases, 'vinecopulib' is licensed
under the MIT License, and 'rvinecopulib' is licensed under the GNU GPL
version 3.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
