%global packname  SpatMCA
%global packver   1.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.0
Release:          2%{?dist}
Summary:          Regularized Spatial Maximum Covariance Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppParallel >= 0.11.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppParallel >= 0.11.2
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fields 
Requires:         R-MASS 

%description
Provide regularized maximum covariance analysis incorporating smoothness,
sparseness and orthogonality of couple patterns by using the alternating
direction method of multipliers algorithm. The method can be applied to
either regularly or irregularly spaced data, including 1D, 2D, and 3D
(Wang and Huang, 2017 <doi:10.1002/env.2481>).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
