%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shiny.element
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Element Plus' Components for 'shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jquerylib 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-uuid 
Requires:         R-stats 
Requires:         R-CRAN-bslib 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-jquerylib 

%description
'Element Plus' ('Vue' 3) components for 'shiny': forms, tables, trees,
menus, dialog boxes and the rest, each reporting to the server and updated
from it like any other 'shiny' input. 'Element Plus' and 'Vue' are
bundled, so applications work offline.

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
