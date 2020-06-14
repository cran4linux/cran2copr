%global packname  cmenet
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Bi-Level Selection of Conditional Main Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-hierNet 
BuildRequires:    R-CRAN-sparsenet 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-hierNet 
Requires:         R-CRAN-sparsenet 

%description
Provides functions for implementing cmenet - a bi-level variable selection
method for conditional main effects (see Mak and Wu (2018)
<doi:10.1080/01621459.2018.1448828>). CMEs are reparametrized interaction
effects which capture the conditional impact of a factor at a fixed level
of another factor. Compared to traditional two-factor interactions, CMEs
can quantify more interpretable interaction effects in many problems. The
current implementation performs variable selection on only binary CMEs; we
are working on an extension for the continuous setting.

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
