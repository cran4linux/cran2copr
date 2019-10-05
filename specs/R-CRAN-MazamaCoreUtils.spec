%global packname  MazamaCoreUtils
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}
Summary:          Utility Functions for Production R Code

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 

%description
A suite of utility functions providing functionality commonly needed for
production level projects such as logging, error handling, and cache
management.

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
