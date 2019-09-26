%global packname  DStree
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Recursive Partitioning for Discrete-Time Survival Trees

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-Ecdat 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-rpart 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-Ecdat 
Requires:         R-CRAN-rpart.plot 
Requires:         R-survival 
Requires:         R-CRAN-Rcpp 

%description
Building discrete-time survival trees and bagged trees based on the
functionalities of the rpart package. Splitting criterion maximizes the
likelihood of a covariate-free logistic discrete time hazard model.

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
