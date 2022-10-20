%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RNeXML
%global packver   2.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Semantically Rich I/O for the 'NeXML' Format

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.95
BuildRequires:    R-CRAN-ape >= 3.1
BuildRequires:    R-methods >= 3.0.0
BuildRequires:    R-CRAN-plyr >= 1.8
BuildRequires:    R-CRAN-reshape2 >= 1.2.2
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.3.1
BuildRequires:    R-CRAN-httr >= 0.3
BuildRequires:    R-CRAN-uuid >= 0.1.1
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-XML >= 3.95
Requires:         R-CRAN-ape >= 3.1
Requires:         R-methods >= 3.0.0
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-reshape2 >= 1.2.2
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.3.1
Requires:         R-CRAN-httr >= 0.3
Requires:         R-CRAN-uuid >= 0.1.1
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rlang 

%description
Provides access to phyloinformatic data in 'NeXML' format.  The package
should add new functionality to R such as the possibility to manipulate
'NeXML' objects in more various and refined way and compatibility with
'ape' objects.

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
