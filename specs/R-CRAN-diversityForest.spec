%global packname  diversityForest
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Diversity Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-Matrix 

%description
Implements diversity forests as described in an upcoming paper by the
author of the package. This package is a fork of the R package 'ranger'
(main author: Marvin N. Wright) that implements random forests using an
efficient C++ implementation. More precisely, 'diversityForest' was
written by modifying the code of 'ranger', version 0.11.0. Therefore,
details on further functionalities of the code that are not presented in
the help pages of 'diversityForest' are found in the help pages of
'ranger' (version 0.11.0). The code in the example sections of the
'diversityForest' manual can be used as a template for all basic
application scenarios with respect to classification, regression and
survival prediction using univariate, binary splitting. Some function
arguments adopted from the 'ranger' package are not be useable with
diversity forests (for the current package version).

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
