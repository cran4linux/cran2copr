%global packname  HDPenReg
%global packver   0.94.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.94.6
Release:          3%{?dist}
Summary:          High-Dimensional Penalized Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-rtkore >= 1.5.5
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-rtkore >= 1.5.5
Requires:         R-methods 
Requires:         R-Matrix 

%description
Algorithms for lasso and fused-lasso problems: implementation of the lars
algorithm for lasso and fusion penalization and EM-based algorithms for
(logistic) lasso and fused-lasso penalization.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
