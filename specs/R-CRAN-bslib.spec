%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bslib
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Custom 'Bootstrap' 'Sass' Themes for 'shiny' and 'rmarkdown'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-fastmap >= 1.1.1
BuildRequires:    R-CRAN-htmltools >= 0.5.8
BuildRequires:    R-CRAN-sass >= 0.4.9
BuildRequires:    R-CRAN-jquerylib >= 0.1.3
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-fastmap >= 1.1.1
Requires:         R-CRAN-htmltools >= 0.5.8
Requires:         R-CRAN-sass >= 0.4.9
Requires:         R-CRAN-jquerylib >= 0.1.3
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-cachem 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-rlang 

%description
Simplifies custom 'CSS' styling of both 'shiny' and 'rmarkdown' via
'Bootstrap' 'Sass'. Supports 'Bootstrap' 3, 4 and 5 as well as their
various 'Bootswatch' themes. An interactive widget is also provided for
previewing themes in real time.

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
