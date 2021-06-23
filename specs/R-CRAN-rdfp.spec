%global __brp_check_rpaths %{nil}
%global packname  rdfp
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          An Implementation of the 'DoubleClick for Publishers' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.19
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-CRAN-curl >= 3.3
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-XML >= 3.98.1.19
Requires:         R-utils >= 3.5.0
Requires:         R-methods >= 3.5.0
Requires:         R-CRAN-curl >= 3.3
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lubridate 

%description
Functions to interact with the 'Google DoubleClick for Publishers (DFP)'
API <https://developers.google.com/ad-manager/api/start> (recently renamed
to 'Google Ad Manager'). This package is automatically compiled from the
API WSDL (Web Service Description Language) files to dictate how the API
is structured. Theoretically, all API actions are possible using this
package; however, care must be taken to format the inputs correctly and
parse the outputs correctly. Please see the 'Google Ad Manager' API
reference <https://developers.google.com/ad-manager/api/rel_notes> and
this package's website <https://stevenmmortimer.github.io/rdfp/> for more
information, documentation, and examples.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
