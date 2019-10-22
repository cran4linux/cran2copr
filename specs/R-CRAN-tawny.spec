%global packname  tawny
%global packver   2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          1%{?dist}
Summary:          Clean Covariance Matrices Using Random Matrix Theory andShrinkage Estimators for Portfolio Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-futile.logger >= 1.3.7
BuildRequires:    R-CRAN-futile.matrix >= 1.2.1
BuildRequires:    R-CRAN-lambda.r >= 1.1.6
BuildRequires:    R-CRAN-tawny.types >= 1.1.2
BuildRequires:    R-CRAN-lambda.tools 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-quantmod 
Requires:         R-CRAN-futile.logger >= 1.3.7
Requires:         R-CRAN-futile.matrix >= 1.2.1
Requires:         R-CRAN-lambda.r >= 1.1.6
Requires:         R-CRAN-tawny.types >= 1.1.2
Requires:         R-CRAN-lambda.tools 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-quantmod 

%description
Portfolio optimization typically requires an estimate of a covariance
matrix of asset returns. There are many approaches for constructing such a
covariance matrix, some using the sample covariance matrix as a starting
point. This package provides implementations for two such methods: random
matrix theory and shrinkage estimation. Each method attempts to clean or
remove noise related to the sampling process from the sample covariance
matrix.

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
