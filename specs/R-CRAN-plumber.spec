%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plumber
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          An API Generator for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-swagger >= 3.33.0
BuildRequires:    R-CRAN-R6 >= 2.0.0
BuildRequires:    R-CRAN-httpuv >= 1.5.5
BuildRequires:    R-CRAN-promises >= 1.1.0
BuildRequires:    R-CRAN-webutils >= 1.1
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-stringi >= 0.3.0
BuildRequires:    R-CRAN-ellipsis >= 0.3.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-swagger >= 3.33.0
Requires:         R-CRAN-R6 >= 2.0.0
Requires:         R-CRAN-httpuv >= 1.5.5
Requires:         R-CRAN-promises >= 1.1.0
Requires:         R-CRAN-webutils >= 1.1
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-stringi >= 0.3.0
Requires:         R-CRAN-ellipsis >= 0.3.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-sodium 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-rlang 

%description
Gives the ability to automatically generate and serve an HTTP API from R
functions using the annotations in the R documentation around your
functions.

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
