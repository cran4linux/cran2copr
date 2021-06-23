%global __brp_check_rpaths %{nil}
%global packname  gargle
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Working with Google APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 2.3.1
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 0.4.9
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli >= 2.3.1
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-rlang >= 0.4.9
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Provides utilities for working with Google APIs
<https://developers.google.com/apis-explorer>.  This includes functions
and classes for handling common credential types and for preparing,
executing, and processing HTTP requests.

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
