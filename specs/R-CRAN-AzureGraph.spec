%global __brp_check_rpaths %{nil}
%global packname  AzureGraph
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Interface to 'Microsoft Graph'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3
BuildRequires:    R-CRAN-AzureAuth >= 1.0.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-httr >= 1.3
Requires:         R-CRAN-AzureAuth >= 1.0.1
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-R6 

%description
A simple interface to the 'Microsoft Graph' API
<https://docs.microsoft.com/en-us/graph/overview>. 'Graph' is a
comprehensive framework for accessing data in various online Microsoft
services. This package was originally intended to provide an R interface
only to the 'Azure Active Directory' part, with a view to supporting
interoperability of R and 'Azure': users, groups, registered apps and
service principals. However it has since been expanded into a more general
tool for interacting with Graph. Part of the 'AzureR' family of packages.

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
