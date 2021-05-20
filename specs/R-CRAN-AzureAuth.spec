%global packname  AzureAuth
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Authentication Services for Azure Active Directory

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-httr >= 1.3
Requires:         R-utils 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jose 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rappdirs 

%description
Provides Azure Active Directory (AAD) authentication functionality for R
users of Microsoft's 'Azure' cloud <https://azure.microsoft.com/>. Use
this package to obtain 'OAuth' 2.0 tokens for services including Azure
Resource Manager, Azure Storage and others. It supports both AAD v1.0 and
v2.0, as well as multiple authentication methods, including device code
and resource owner grant. Tokens are cached in a user-specific directory
obtained using the 'rappdirs' package. The interface is based on the
'OAuth' framework in the 'httr' package, but customised and streamlined
for Azure. Part of the 'AzureR' family of packages.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
