%global packname  PortfolioEffectEstim
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          High Frequency Price Estimators by PortfolioEffect

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PortfolioEffectHFT >= 1.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-PortfolioEffectHFT >= 1.7
Requires:         R-methods 
Requires:         R-CRAN-rJava 

%description
R interface to PortfolioEffect cloud service for estimating high frequency
price variance, quarticity, microstructure noise variance, and other
metrics in both aggregate and rolling window flavors. Constructed
estimators could use client-side market data or access HF intraday price
history for all major US Equities. See <https://www.portfolioeffect.com/>
for more information on the PortfolioEffect high frequency portfolio
analytics platform.

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
