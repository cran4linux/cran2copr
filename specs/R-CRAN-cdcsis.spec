%global __brp_check_rpaths %{nil}
%global packname  cdcsis
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Conditional Distance Correlation Based Feature Screening andConditional Independence Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-ks >= 1.8.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ks >= 1.8.0
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Conditional distance correlation <doi:10.1080/01621459.2014.993081> is a
novel conditional dependence measurement of two multivariate random
variables given a confounding variable. This package provides conditional
distance correlation, performs the conditional distance correlation sure
independence screening procedure for ultrahigh dimensional data
<http://www3.stat.sinica.edu.tw/statistica/J28N1/J28N114/J28N114.html>,
and conducts conditional distance covariance test for conditional
independence assumption of two multivariate variable.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
