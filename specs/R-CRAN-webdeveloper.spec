%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  webdeveloper
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Web Development

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-html5 >= 1.0.0
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-html5 >= 1.0.0
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-future 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringi 

%description
Organizational framework for web development in R including functions to
serve static and dynamic content via HTTP methods, includes the html5
package to create HTML pages, and offers other utility functions for
common tasks related to web development.

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
