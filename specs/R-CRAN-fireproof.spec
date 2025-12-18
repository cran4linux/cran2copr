%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fireproof
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Authentication and Authorization for 'fiery' Servers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reqres >= 1.1.0
BuildRequires:    R-CRAN-routr >= 1.0.0
BuildRequires:    R-CRAN-firesale >= 0.1.1
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fiery 
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-urltools 
Requires:         R-CRAN-reqres >= 1.1.0
Requires:         R-CRAN-routr >= 1.0.0
Requires:         R-CRAN-firesale >= 0.1.1
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fiery 
Requires:         R-CRAN-jose 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sodium 
Requires:         R-CRAN-urltools 

%description
Provides a plugin for 'fiery' that supports various forms of authorization
and authentication schemes. Schemes can be required in various
combinations or by themselves and can be combined with scopes to provide
fine-grained access control to the server.

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
