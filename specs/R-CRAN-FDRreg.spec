%global packname  FDRreg
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          False discovery rate regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-splines >= 3.0.2
BuildRequires:    R-CRAN-fda >= 2.4.0
BuildRequires:    R-CRAN-mosaic >= 0.8.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-splines >= 3.0.2
Requires:         R-CRAN-fda >= 2.4.0
Requires:         R-CRAN-mosaic >= 0.8.10
Requires:         R-CRAN-Rcpp >= 0.11.0

%description
Tools for FDR problems, including false discovery rate regression. See
corresponding paper: "False discovery rate regression: application to
neural synchrony detection in primary visual cortex."  James G. Scott,
Ryan C. Kelly, Matthew A. Smith, Robert E. Kass.

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
