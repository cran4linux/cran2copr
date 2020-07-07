%global packname  emstreeR
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}
Summary:          Tools for Fast Computing and Plotting Euclidean Minimum SpanningTrees

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-RcppMLPACK 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-BBmisc 

%description
Computes Euclidean Minimum Spanning Trees (EMST) using the fast Dual-Tree
Boruvka algorithm (March, Ram, Gray, 2010, <doi:10.1145/1835804.1835882>)
implemented in 'mlpack' - the C++ Machine Learning library (Curtin et al.,
2013). 'emstreeR' heavily relies on 'RcppMLPACK' and 'Rcpp', working as a
wrapper to the C++ fast EMST algorithm. Thus, R users do not have to deal
with the R-'Rcpp'-C++ integration. The package also provides functions and
an S3 method for readily plotting Minimum Spanning Trees (MST) using
either 'base' R, 'scatterplot3d' or 'ggplot2' style.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%doc %{rlibdir}/%{packname}/lib
