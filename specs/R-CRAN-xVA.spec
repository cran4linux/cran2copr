%global packname  xVA
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}
Summary:          Calculates Credit Risk Valuation Adjustments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SACCR 
BuildRequires:    R-CRAN-Trading 
Requires:         R-methods 
Requires:         R-CRAN-SACCR 
Requires:         R-CRAN-Trading 

%description
Calculates a number of valuation adjustments including CVA, DVA, FBA, FCA,
MVA and KVA. A two-way margin agreement has been implemented. For the KVA
calculation three regulatory frameworks are supported: CEM, SA-CCR and
IMM. The probability of default is implied through the credit spreads
curve. Currently, only IRSwaps are supported. For more information, you
can check one of the books regarding xVA:
<http://www.cvacentral.com/books/credit-value-adjustment>.

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
