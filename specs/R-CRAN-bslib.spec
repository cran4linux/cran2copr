%global packname  bslib
%global packver   0.2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Custom 'Bootstrap' 'Sass' Themes for 'shiny' and 'rmarkdown'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools >= 0.5.1
BuildRequires:    R-CRAN-sass >= 0.4.0
BuildRequires:    R-CRAN-jquerylib >= 0.1.3
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-htmltools >= 0.5.1
Requires:         R-CRAN-sass >= 0.4.0
Requires:         R-CRAN-jquerylib >= 0.1.3
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
Simplifies custom 'CSS' styling of both 'shiny' and 'rmarkdown' via
'Bootstrap' 'Sass'. Supports both 'Bootstrap' 3 and 4 as well as their
various 'Bootswatch' themes. An interactive widget is also provided for
previewing themes in real time.

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
