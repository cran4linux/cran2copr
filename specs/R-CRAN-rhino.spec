%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rhino
%global packver   1.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Enterprise Shiny Applications

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lintr >= 3.0.0
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-box >= 1.1.3
BuildRequires:    R-CRAN-box.linters >= 0.10.5
BuildRequires:    R-CRAN-box.lsp 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-sass 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-styler 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-lintr >= 3.0.0
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-box >= 1.1.3
Requires:         R-CRAN-box.linters >= 0.10.5
Requires:         R-CRAN-box.lsp 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-config 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-sass 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-styler 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
A framework that supports creating and extending enterprise Shiny
applications using best practices.

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
