%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.modules.clinical
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          'teal' Modules for Standard Clinical Outputs

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rmarkdown >= 2.19
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-tern >= 0.9.3
BuildRequires:    R-CRAN-broom >= 0.7.10
BuildRequires:    R-CRAN-rtables >= 0.6.6
BuildRequires:    R-CRAN-formatters >= 0.5.5
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.1
BuildRequires:    R-CRAN-teal.transform >= 0.5.0
BuildRequires:    R-CRAN-teal.code >= 0.5.0
BuildRequires:    R-CRAN-teal.data >= 0.4.0
BuildRequires:    R-CRAN-teal.widgets >= 0.4.0
BuildRequires:    R-CRAN-tern.mmrm >= 0.3.0
BuildRequires:    R-CRAN-rlistings >= 0.2.7
BuildRequires:    R-CRAN-teal.reporter >= 0.2.1
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-logger >= 0.2.0
BuildRequires:    R-CRAN-teal >= 0.15.0
BuildRequires:    R-CRAN-DT >= 0.13
BuildRequires:    R-CRAN-tern.gee >= 0.1.3
BuildRequires:    R-CRAN-teal.logger >= 0.1.1
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyvalidate 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vistime 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rmarkdown >= 2.19
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-tern >= 0.9.3
Requires:         R-CRAN-broom >= 0.7.10
Requires:         R-CRAN-rtables >= 0.6.6
Requires:         R-CRAN-formatters >= 0.5.5
Requires:         R-CRAN-shinyWidgets >= 0.5.1
Requires:         R-CRAN-teal.transform >= 0.5.0
Requires:         R-CRAN-teal.code >= 0.5.0
Requires:         R-CRAN-teal.data >= 0.4.0
Requires:         R-CRAN-teal.widgets >= 0.4.0
Requires:         R-CRAN-tern.mmrm >= 0.3.0
Requires:         R-CRAN-rlistings >= 0.2.7
Requires:         R-CRAN-teal.reporter >= 0.2.1
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-logger >= 0.2.0
Requires:         R-CRAN-teal >= 0.15.0
Requires:         R-CRAN-DT >= 0.13
Requires:         R-CRAN-tern.gee >= 0.1.3
Requires:         R-CRAN-teal.logger >= 0.1.1
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyvalidate 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vistime 

%description
Provides user-friendly tools for creating and customizing clinical trial
reports. By leveraging the 'teal' framework, this package provides 'teal'
modules to easily create an interactive panel that allows for seamless
adjustments to data presentation, thereby streamlining the creation of
detailed and accurate reports.

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
