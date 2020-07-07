%global packname  bigtime
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Sparse Estimation of Large Time Series Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-zoo 
Requires:         R-lattice 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-corrplot 

%description
Estimation of large Vector AutoRegressive (VAR), Vector AutoRegressive
with Exogenous Variables X (VARX) and Vector AutoRegressive Moving Average
(VARMA) Models with Structured Lasso Penalties, see Nicholson, Bien and
Matteson (2017) <arXiv:1412.5250v2> and Wilms, Basu, Bien and Matteson
(2017) <arXiv:1707.09208>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
