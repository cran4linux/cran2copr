%global packname  TDA
%global packver   1.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.9
Release:          3%{?dist}
Summary:          Statistical Tools for Topological Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
Requires:         gmp
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-scales 

%description
Tools for the statistical analysis of persistent homology and for density
clustering. For that, this package provides an R interface for the
efficient algorithms of the C++ libraries 'GUDHI'
<http://gudhi.gforge.inria.fr/>, 'Dionysus'
<http://www.mrzv.org/software/dionysus/>, and 'PHAT'
<https://bitbucket.org/phat-code/phat/>. This package also implements the
methods in Fasy et al. (2014) <doi:10.1214/14-AOS1252> and Chazal et al.
(2014) <doi:10.1145/2582112.2582128> for analyzing the statistical
significance of persistent homology features.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
