%global packname  AzureKusto
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Interface to 'Kusto'/'Azure Data Explorer'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-AzureRMR >= 2.0.0
BuildRequires:    R-CRAN-httr >= 1.3
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 0.2.4
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-AzureAuth 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-AzureRMR >= 2.0.0
Requires:         R-CRAN-httr >= 1.3
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-tidyselect >= 0.2.4
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-AzureAuth 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 

%description
An interface to 'Azure Data Explorer', also known as 'Kusto', a fast,
highly scalable data exploration service from Microsoft:
<https://azure.microsoft.com/en-us/services/data-explorer/>. Includes
'DBI' and 'dplyr' interfaces, with the latter modelled after the 'dbplyr'
package, whereby queries are translated from R into the native 'KQL' query
language and executed lazily. On the admin side, the package extends the
object framework provided by 'AzureRMR' to support creation and deletion
of databases, and management of database principals. Part of the 'AzureR'
family of packages.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
