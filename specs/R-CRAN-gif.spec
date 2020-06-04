%global packname  gif
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Graphical Independence Filtering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-MASS 
Requires:         R-Matrix 

%description
Provides a method of recovering the precision matrix for Gaussian
graphical models efficiently. Our approach could be divided into three
categories. First of all, we use Hard Graphical Thresholding for best
subset selection problem of Gaussian graphical model, and the core concept
of this method was proposed by Luo et al. (2014) <arXiv:1407.7819>.
Secondly, a closed form solution for graphical lasso under acyclic graph
structure is implemented in our package (Fattahi and Sojoudi (2019)
<http://jmlr.org/papers/v20/17-501.html>). Furthermore, we implement block
coordinate descent algorithm to efficiently solve the covariance selection
problem (Dempster (1972) <doi:10.2307/2528966>). Our package is
computationally efficient and can solve ultra-high-dimensional problems,
e.g. p > 10,000, in a few minutes.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
