%global packname  PMwR
%global packver   0.14-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.0
Release:          1%{?dist}
Summary:          Portfolio Management with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-CRAN-datetimeutils 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-orgutils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-NMOF 
Requires:         R-CRAN-datetimeutils 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-orgutils 
Requires:         R-parallel 
Requires:         R-CRAN-textutils 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Functions and examples for 'Portfolio Management with R': backtesting
investment and trading strategies, computing profit/loss and returns,
analysing trades, handling lists of transactions, reporting, and more.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
