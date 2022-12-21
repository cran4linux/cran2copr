%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bs4Dash
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'Bootstrap 4' Version of 'shinydashboard'

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-httpuv >= 1.5.2
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-htmltools >= 0.5.1.1
BuildRequires:    R-CRAN-bslib >= 0.2.4
BuildRequires:    R-CRAN-waiter >= 0.2.3
BuildRequires:    R-CRAN-fresh 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-httpuv >= 1.5.2
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-htmltools >= 0.5.1.1
Requires:         R-CRAN-bslib >= 0.2.4
Requires:         R-CRAN-waiter >= 0.2.3
Requires:         R-CRAN-fresh 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-httr 

%description
Make 'Bootstrap 4' Shiny dashboards. Use the full power of 'AdminLTE3', a
dashboard template built on top of 'Bootstrap 4'
<https://github.com/ColorlibHQ/AdminLTE>.

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
