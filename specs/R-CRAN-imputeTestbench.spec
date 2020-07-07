%global packname  imputeTestbench
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          3%{?dist}
Summary:          Test Bench for the Comparison of Imputation Methods

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-imputeTS 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 

%description
Provides a test bench for the comparison of missing data imputation
methods in uni-variate time series. Imputation methods are compared using
different error metrics. Proposed imputation methods and alternative error
metrics can be used.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
