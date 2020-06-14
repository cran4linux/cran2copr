%global packname  Riex
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          IEX Stocks and Market Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-urltools >= 1.7.1
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-tidyverse >= 1.2.1
BuildRequires:    R-CRAN-quantmod >= 0.4.14
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rjson >= 0.2.20
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-urltools >= 1.7.1
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-tidyverse >= 1.2.1
Requires:         R-CRAN-quantmod >= 0.4.14
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rjson >= 0.2.20
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 

%description
Retrieves efficiently and reliably Investors Exchange ('IEX') stock and
market data using 'IEX Cloud API'. The platform is offered by Investors
Exchange Group (IEX Group). Main goal is to leverage 'R' capabilities
including existing packages to effectively provide financial and
statistical analysis as well as visualization in support of fact-based
decisions. In addition, continuously improve and enhance 'Riex' by
applying best practices and being in tune with users' feedback and
requirements. Please, make sure to review and acknowledge Investors
Exchange Group (IEX Group) terms and conditions before using 'Riex'
(<https://iexcloud.io/terms/>).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
