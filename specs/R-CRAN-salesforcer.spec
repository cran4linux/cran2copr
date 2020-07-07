%global packname  salesforcer
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          An Implementation of 'Salesforce' APIs Using Tidy Principles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.99.0.3
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-XML >= 3.99.0.3
Requires:         R-methods >= 3.6.0
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-zip 

%description
Functions connecting to the 'Salesforce' Platform APIs (REST, SOAP, Bulk
1.0, Bulk 2.0, and Metadata)
<https://trailhead.salesforce.com/en/content/learn/modules/api_basics/api_basics_overview>.
Most all calls from these APIs are supported as they use CSV, XML or JSON
data that can be parsed into R data structures. For more details please
see the 'Salesforce' API documentation and this package's website
<https://stevenmmortimer.github.io/salesforcer/> for more information,
documentation, and examples.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
