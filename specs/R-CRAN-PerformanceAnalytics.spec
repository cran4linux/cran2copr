%global packname  PerformanceAnalytics
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          2%{?dist}
Summary:          Econometric Tools for Performance and Risk Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-xts >= 0.10.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-xts >= 0.10.0
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-zoo 

%description
Collection of econometric functions for performance and risk analysis. In
addition to standard risk and performance metrics, this package aims to
aid practitioners and researchers in utilizing the latest research in
analysis of non-normal return streams.  In general, it is most tested on
return (rather than price) data on a regular scale, but most functions
will work with irregular return data as well, and increasing numbers of
functions will work with P&L or price data where possible.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
