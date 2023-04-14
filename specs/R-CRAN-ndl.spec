%global __brp_check_rpaths %{nil}
%global packname  ndl
%global packver   0.2.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.18
Release:          3%{?dist}%{?buildtag}
Summary:          Naive Discriminative Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-MASS 
Requires:         R-CRAN-Hmisc 

%description
Naive discriminative learning implements learning and classification
models based on the Rescorla-Wagner equations and their equilibrium
equations.

%prep
%setup -q -c -n %{packname}
find %{packname}/inst -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
