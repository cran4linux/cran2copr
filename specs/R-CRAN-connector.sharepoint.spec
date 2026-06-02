%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  connector.sharepoint
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Microsoft SharePoint' Interface for the 'connector' Package

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-connector >= 1.0.0
BuildRequires:    R-CRAN-AzureAuth 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Microsoft365R 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-zephyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-connector >= 1.0.0
Requires:         R-CRAN-AzureAuth 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Microsoft365R 
Requires:         R-CRAN-R6 
Requires:         R-tools 
Requires:         R-CRAN-zephyr 
Requires:         R-CRAN-rlang 

%description
Extends the 'connector' package to provide a convenient interface for
accessing and interacting with 'Microsoft SharePoint' directly from 'R'.
Supports listing, reading, writing, uploading, downloading, and removing
files and directories on 'SharePoint' document libraries. Authentication
is handled through 'Azure' tokens via the 'AzureAuth' package.

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
