%global __brp_check_rpaths %{nil}
%global packname  AzureRMR
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'Azure Resource Manager'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3
BuildRequires:    R-CRAN-AzureAuth >= 1.2.1
BuildRequires:    R-CRAN-AzureGraph >= 1.2.0
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-httr >= 1.3
Requires:         R-CRAN-AzureAuth >= 1.2.1
Requires:         R-CRAN-AzureGraph >= 1.2.0
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-uuid 

%description
A lightweight but powerful R interface to the 'Azure Resource Manager'
REST API. The package exposes a comprehensive class framework and related
tools for creating, updating and deleting 'Azure' resource groups,
resources and templates. While 'AzureRMR' can be used to manage any
'Azure' service, it can also be extended by other packages to provide
extra functionality for specific services. Part of the 'AzureR' family of
packages.

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
