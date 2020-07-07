%global packname  quadrupen
%global packver   0.2-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          3%{?dist}
Summary:          Sparsity by Worst-Case Quadratic Penalties

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grid 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-grid 
Requires:         R-parallel 

%description
Fits classical sparse regression models with efficient active set
algorithms by solving quadratic problems as described in
<arXiv:1210.2077>. Also provides a few methods for model selection purpose
(cross-validation, stability selection).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
