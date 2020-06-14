%global packname  QFRM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Pricing of Vanilla and Exotic Option Contracts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 

%description
Option pricing (financial derivatives) techniques mainly following
textbook 'Options, Futures and Other Derivatives', 9ed by John C.Hull,
2014. Prentice Hall. Implementations are via binomial tree option model
(BOPM), Black-Scholes model, Monte Carlo simulations, etc. This package is
a result of Quantitative Financial Risk Management course (STAT 449 and
STAT 649) at Rice University, Houston, TX, USA, taught by Oleg Melnikov,
statistics PhD student, as of Spring 2015.

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
%{rlibdir}/%{packname}/INDEX
