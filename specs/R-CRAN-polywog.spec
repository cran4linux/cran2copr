%global packname  polywog
%global packver   0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}
Summary:          Bootstrapped Basis Regression with Oracle Model Selection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ncvreg >= 2.4.0
BuildRequires:    R-CRAN-glmnet >= 1.9.5
BuildRequires:    R-CRAN-miscTools >= 0.6.12
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ncvreg >= 2.4.0
Requires:         R-CRAN-glmnet >= 1.9.5
Requires:         R-CRAN-miscTools >= 0.6.12
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-iterators 
Requires:         R-Matrix 
Requires:         R-CRAN-stringr 

%description
Routines for flexible functional form estimation via basis regression,
with model selection via the adaptive LASSO or SCAD to prevent
overfitting.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
