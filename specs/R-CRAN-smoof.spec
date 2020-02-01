%global packname  smoof
%global packver   1.6.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0.1
Release:          1%{?dist}
Summary:          Single and Multi-Objective Optimization Test Functions

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-ParamHelpers >= 1.8
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-checkmate >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-mco 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-ParamHelpers >= 1.8
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-checkmate >= 1.1
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-mco 
Requires:         R-CRAN-RJSONIO 

%description
Provides generators for a high number of both single- and multi- objective
test functions which are frequently used for the benchmarking of
(numerical) optimization algorithms. Moreover, it offers a set of
convenient functions to generate, plot and work with objective functions.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/mpm2.py
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
