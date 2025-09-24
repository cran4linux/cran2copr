%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtiddlywiki
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for 'TiddlyWiki'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.2.0
BuildRequires:    R-CRAN-settings 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-websocket 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-httr2 >= 1.2.0
Requires:         R-CRAN-settings 
Requires:         R-stats 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-websocket 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-later 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmltools 
Requires:         R-grDevices 

%description
'TiddlyWiki' is a unique non-linear notebook for capturing, organising and
sharing complex information. 'rtiddlywiki' is a R interface of
'TiddlyWiki' <https://tiddlywiki.com> to create new tiddler from Rmarkdown
file, and then put into a local 'TiddlyWiki' node.js server if it is
available.

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
