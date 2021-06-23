%global __brp_check_rpaths %{nil}
%global packname  fuser
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Fused Lasso for High-Dimensional Regression over Groups

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-RSpectra 

%description
Enables high-dimensional penalized regression across heterogeneous
subgroups. Fusion penalties are used to share information about the linear
parameters across subgroups. The underlying model is described in detail
in Dondelinger and Mukherjee (2017) <arXiv:1611.00953>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
