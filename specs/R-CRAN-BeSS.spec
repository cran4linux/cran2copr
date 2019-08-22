%global packname  BeSS
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Best Subset Selection in Linear, Logistic and CoxPH Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-CRAN-glmnet 
Requires:         R-survival 

%description
An implementation of best subset selection in generalized linear model and
Cox proportional hazard model via the primal dual active set algorithm
proposed by Wen, C., Zhang, A., Quan, S. and Wang, X. (2017)
<arXiv:1709.06254>. The algorithm formulates coefficient parameters and
residuals as primal and dual variables and utilizes efficient active set
selection strategies based on the complementarity of the primal and dual
variables.

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
