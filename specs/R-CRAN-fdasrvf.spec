%global packname  fdasrvf
%global packver   1.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.3
Release:          2%{?dist}
Summary:          Elastic Functional Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-splines 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-tolerance 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-coda 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 
Requires:         R-splines 
Requires:         R-parallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-tolerance 
Requires:         R-CRAN-testthat 

%description
Performs alignment, PCA, and modeling of multidimensional and
unidimensional functions using the square-root velocity framework
(Srivastava et al., 2011 <arXiv:1103.3817> and Tucker et al., 2014
<DOI:10.1016/j.csda.2012.12.001>). This framework allows for elastic
analysis of functional data through phase and amplitude separation.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
