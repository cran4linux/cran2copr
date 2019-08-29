%global packname  bigKRLS
%global packver   3.0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.5.1
Release:          1%{?dist}
Summary:          Optimized Kernel Regularized Least Squares

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-bigalgebra 
BuildRequires:    R-CRAN-biganalytics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-bigalgebra 
Requires:         R-CRAN-biganalytics 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-shiny 

%description
Functions for Kernel-Regularized Least Squares optimized for speed and
memory usage are provided along with visualization tools. For working
papers, sample code, and recent presentations visit
<https://sites.google.com/site/petemohanty/software/>. bigKRLS, as well
its dependencies, require current versions of R and its compilers (and
RStudio if used). For details, see
<https://github.com/rdrr1990/bigKRLS/blob/master/INSTALL.md>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
