%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.modules.clinical
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          'teal' Modules for Standard Clinical Outputs

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rmarkdown >= 2.23
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-scales >= 1.4.0
BuildRequires:    R-CRAN-vistime >= 1.2.3
BuildRequires:    R-CRAN-shinyjs >= 1.10.0
BuildRequires:    R-CRAN-teal >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-tern >= 0.9.9
BuildRequires:    R-CRAN-ggrepel >= 0.9.6
BuildRequires:    R-CRAN-bslib >= 0.8.0
BuildRequires:    R-CRAN-teal.data >= 0.8.0
BuildRequires:    R-CRAN-broom >= 0.7.10
BuildRequires:    R-CRAN-teal.transform >= 0.7.0
BuildRequires:    R-CRAN-cowplot >= 0.7.0
BuildRequires:    R-CRAN-teal.code >= 0.7.0
BuildRequires:    R-CRAN-rtables >= 0.6.13
BuildRequires:    R-CRAN-teal.reporter >= 0.6.0
BuildRequires:    R-CRAN-formatters >= 0.5.11
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.1
BuildRequires:    R-CRAN-teal.widgets >= 0.5.0
BuildRequires:    R-CRAN-teal.logger >= 0.4.0
BuildRequires:    R-CRAN-tern.mmrm >= 0.3.3
BuildRequires:    R-CRAN-rlistings >= 0.2.12
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-DT >= 0.13
BuildRequires:    R-CRAN-tern.gee >= 0.1.5
BuildRequires:    R-CRAN-shinyvalidate >= 0.1.3
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rmarkdown >= 2.23
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-scales >= 1.4.0
Requires:         R-CRAN-vistime >= 1.2.3
Requires:         R-CRAN-shinyjs >= 1.10.0
Requires:         R-CRAN-teal >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-tern >= 0.9.9
Requires:         R-CRAN-ggrepel >= 0.9.6
Requires:         R-CRAN-bslib >= 0.8.0
Requires:         R-CRAN-teal.data >= 0.8.0
Requires:         R-CRAN-broom >= 0.7.10
Requires:         R-CRAN-teal.transform >= 0.7.0
Requires:         R-CRAN-cowplot >= 0.7.0
Requires:         R-CRAN-teal.code >= 0.7.0
Requires:         R-CRAN-rtables >= 0.6.13
Requires:         R-CRAN-teal.reporter >= 0.6.0
Requires:         R-CRAN-formatters >= 0.5.11
Requires:         R-CRAN-shinyWidgets >= 0.5.1
Requires:         R-CRAN-teal.widgets >= 0.5.0
Requires:         R-CRAN-teal.logger >= 0.4.0
Requires:         R-CRAN-tern.mmrm >= 0.3.3
Requires:         R-CRAN-rlistings >= 0.2.12
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-DT >= 0.13
Requires:         R-CRAN-tern.gee >= 0.1.5
Requires:         R-CRAN-shinyvalidate >= 0.1.3
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

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
