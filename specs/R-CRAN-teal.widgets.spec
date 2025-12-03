%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.widgets
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Widgets for 'teal' Applications

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.3
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-styler >= 1.2.0
BuildRequires:    R-CRAN-bslib >= 0.8.0
BuildRequires:    R-CRAN-rtables >= 0.6.12
BuildRequires:    R-CRAN-htmltools >= 0.5.4
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.1
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.4.3
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-styler >= 1.2.0
Requires:         R-CRAN-bslib >= 0.8.0
Requires:         R-CRAN-rtables >= 0.6.12
Requires:         R-CRAN-htmltools >= 0.5.4
Requires:         R-CRAN-shinyWidgets >= 0.5.1
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Collection of 'shiny' widgets to support 'teal' applications. Enables the
manipulation of application layout and plot or table settings.

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
