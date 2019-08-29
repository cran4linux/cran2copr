%global packname  FRegSigCom
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Functional Regression using Signal Compression Approach

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-fda 
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 

%description
Signal compression methods for functional regression. It includes various
function-on-function (FOF) regression models such as the linear FOF model
with functional response and both scalar and functional predictors for a
small number of functional predictors, linear FOF models with a large
number of functional predictors, linear FOF model for spiky data, stepwise
selection for FOF models with two-way interactions, and nonlinear FOF
models. It also includes scalar-on-function regression models with single
(SOF) or multivariate (mSOF) scalar response variable, and SOF model for
spiky data.

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
