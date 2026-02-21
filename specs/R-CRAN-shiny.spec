%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shiny
%global packver   1.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          Web Application Framework for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-commonmark >= 2.0.0
BuildRequires:    R-CRAN-R6 >= 2.0
BuildRequires:    R-CRAN-httpuv >= 1.5.2
BuildRequires:    R-CRAN-promises >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-fastmap >= 1.1.1
BuildRequires:    R-CRAN-cachem >= 1.1.0
BuildRequires:    R-CRAN-later >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-bslib >= 0.6.0
BuildRequires:    R-CRAN-htmltools >= 0.5.4
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-fontawesome >= 0.4.0
BuildRequires:    R-CRAN-mime >= 0.3
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-otel 
BuildRequires:    R-CRAN-sourcetools 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-commonmark >= 2.0.0
Requires:         R-CRAN-R6 >= 2.0
Requires:         R-CRAN-httpuv >= 1.5.2
Requires:         R-CRAN-promises >= 1.5.0
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-fastmap >= 1.1.1
Requires:         R-CRAN-cachem >= 1.1.0
Requires:         R-CRAN-later >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-bslib >= 0.6.0
Requires:         R-CRAN-htmltools >= 0.5.4
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-fontawesome >= 0.4.0
Requires:         R-CRAN-mime >= 0.3
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-methods 
Requires:         R-CRAN-cli 
Requires:         R-grDevices 
Requires:         R-CRAN-otel 
Requires:         R-CRAN-sourcetools 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xtable 

%description
Makes it incredibly easy to build interactive web applications with R.
Automatic "reactive" binding between inputs and outputs and extensive
prebuilt widgets make it possible to build beautiful, responsive, and
powerful applications with minimal effort.

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
