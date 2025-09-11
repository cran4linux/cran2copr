%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AzureKusto
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-tidyr 
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
Requires:         R-CRAN-tidyr 

%description
An interface to 'Azure Data Explorer', also known as 'Kusto', a fast,
distributed data exploration service from Microsoft:
<https://azure.microsoft.com/en-us/products/data-explorer/>. Includes
'DBI' and 'dplyr' interfaces, with the latter modelled after the 'dbplyr'
package, whereby queries are translated from R into the native 'KQL' query
language and executed lazily. On the admin side, the package extends the
object framework provided by 'AzureRMR' to support creation and deletion
of databases, and management of database principals. Part of the 'AzureR'
family of packages.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
