%global packname  rootWishart
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}
Summary:          Distribution of Largest Root for Single and Double WishartSettings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 

%description
Functions for hypothesis testing in single and double Wishart settings,
based on Roy's largest root. This test statistic is especially useful in
multivariate analysis. The computations are based on results by Chiani
(2014) <DOI:10.1016/j.jmva.2014.04.002> and Chiani (2016)
<DOI:10.1016/j.jmva.2015.10.007>. They use the fact that the CDF is
related to the Pfaffian of a matrix that can be computed in a finite
number of iterations. This package takes advantage of the Boost and Eigen
C++ libraries to perform multi-precision linear algebra.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
