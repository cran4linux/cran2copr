%global packname  egcm
%global packver   1.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          2%{?dist}
Summary:          Engle-Granger Cointegration Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tseries 
Requires:         R-MASS 
Requires:         R-CRAN-urca 
Requires:         R-parallel 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-quantmod 
Requires:         R-methods 

%description
An easy-to-use implementation of the Engle-Granger two-step procedure for
identifying pairs of cointegrated series.  It is geared towards the
analysis of pairs of securities.  Summary and plot functions are provided,
and the package is able to fetch closing prices of securities from Yahoo.
A variety of unit root tests are supported, and an improved unit root test
is included.

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
