%global packname  SACCR
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          2%{?dist}
Summary:          SA Counterparty Credit Risk under Basel III

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Trading 
Requires:         R-methods 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Trading 

%description
Computes the Exposure-At-Default based on standardized approach of the
Basel III Regulatory framework (SA-CCR). Currently, trade types of all the
five major asset classes have been created and, given the inheritance-
based structure of the application, the addition of further trade types is
straightforward. The application returns a list of trees (one per CSA)
after automatically separating the trades based on the CSAs, the hedging
sets, the netting sets and the risk factors. The basis and volatility
transactions are also identified and treated in specific hedging sets
whereby the corresponding penalty factors are applied. All the examples
appearing on the regulatory paper (including the margined and the
un-margined workflow) have been implemented including the latest FAQ
enhancements.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
