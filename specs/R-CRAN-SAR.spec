%global packname  SAR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Smart Adaptive Recommendations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-Rcpp >= 0.12
BuildRequires:    R-CRAN-AzureRMR 
BuildRequires:    R-CRAN-AzureStor 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-Rcpp >= 0.12
Requires:         R-CRAN-AzureRMR 
Requires:         R-CRAN-AzureStor 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-Matrix 
Requires:         R-CRAN-R6 
Requires:         R-parallel 
Requires:         R-CRAN-RcppParallel 

%description
'Smart Adaptive Recommendations' (SAR) is the name of a fast, scalable,
adaptive algorithm for personalized recommendations based on user
transactions and item descriptions. It produces easily
explainable/interpretable recommendations and handles "cold item" and
"semi-cold user" scenarios. This package provides two implementations of
'SAR': a standalone implementation, and an interface to a web service in
Microsoft's 'Azure' cloud:
<https://github.com/Microsoft/Product-Recommendations/blob/master/doc/sar.md>.
The former allows fast and easy experimentation, and the latter provides
robust scalability and extra features for production use.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
