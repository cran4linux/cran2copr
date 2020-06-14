%global packname  partialCI
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Partial Cointegration

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-partialAR 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-KFAS 
Requires:         R-CRAN-partialAR 
Requires:         R-CRAN-zoo 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-MASS 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glmnet 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-KFAS 

%description
A collection of time series is partially cointegrated if a linear
combination of these time series can be found so that the residual spread
is partially autoregressive - meaning that it can be represented as a sum
of an autoregressive series and a random walk. This concept is useful in
modeling certain sets of financial time series and beyond, as it allows
for the spread to contain transient and permanent components alike.
Partial cointegration has been introduced by Clegg and Krauss (2017)
<doi:10.1080/14697688.2017.1370122>, along with a large-scale empirical
application to financial market data. The partialCI package comprises
estimation, testing, and simulation routines for partial cointegration
models in state space. Clegg et al. (2017)
<https://hdl.handle.net/10419/150014> provide an in in-depth discussion of
the package functionality as well as illustrating examples in the fields
of finance and macroeconomics.

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
