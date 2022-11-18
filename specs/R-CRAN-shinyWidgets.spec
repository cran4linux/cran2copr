%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyWidgets
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Custom Inputs Widgets for Shiny

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-htmltools >= 0.5.1
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-sass 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-htmltools >= 0.5.1
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-sass 
Requires:         R-CRAN-jsonlite 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 

%description
Collection of custom input controls and user interface components for
'Shiny' applications. Give your applications a unique and colorful style !

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
