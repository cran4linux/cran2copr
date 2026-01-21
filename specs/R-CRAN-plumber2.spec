%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plumber2
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy and Powerful Web Servers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-routr >= 2.0.0
BuildRequires:    R-CRAN-fiery >= 1.5.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-reqres >= 1.0.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fireproof 
BuildRequires:    R-CRAN-firesafety 
BuildRequires:    R-CRAN-firesale 
BuildRequires:    R-CRAN-firestorm 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-rapidoc 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-webutils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-routr >= 2.0.0
Requires:         R-CRAN-fiery >= 1.5.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-reqres >= 1.0.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fireproof 
Requires:         R-CRAN-firesafety 
Requires:         R-CRAN-firesale 
Requires:         R-CRAN-firestorm 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-rapidoc 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-svglite 
Requires:         R-utils 
Requires:         R-CRAN-webutils 
Requires:         R-CRAN-yaml 

%description
Automatically create a web server from annotated 'R' files or by building
it up programmatically. Provides automatic 'OpenAPI' documentation, input
handling, asynchronous evaluation, and plugin support.

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
