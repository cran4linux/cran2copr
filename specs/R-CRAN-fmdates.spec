%global packname  fmdates
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          Financial Market Date Calculations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-assertthat 
Requires:         R-methods 
Requires:         R-utils 

%description
Implements common date calculations relevant for specifying the economic
nature of financial market contracts that are typically defined by
International Swap Dealer Association (ISDA, <http://www2.isda.org>) legal
documentation. This includes methods to check whether dates are business
days in certain locales, functions to adjust and shift dates and time
length (or day counter) calculations.

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
