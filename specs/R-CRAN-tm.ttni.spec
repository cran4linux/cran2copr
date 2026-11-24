%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tm.ttni
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'teal' Module for Time-to-Next-Intervention and Time-to-Event Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-teal >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-tern >= 0.9.0
BuildRequires:    R-CRAN-rtables >= 0.6.0
BuildRequires:    R-CRAN-teal.widgets >= 0.4.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-shinyvalidate >= 0.1.0
BuildRequires:    R-CRAN-teal.picks >= 0.1.0
BuildRequires:    R-stats 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-teal >= 1.2.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-tern >= 0.9.0
Requires:         R-CRAN-rtables >= 0.6.0
Requires:         R-CRAN-teal.widgets >= 0.4.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-shinyvalidate >= 0.1.0
Requires:         R-CRAN-teal.picks >= 0.1.0
Requires:         R-stats 

%description
Provides an open-source 'teal' module and a reusable table builder for
time to next intervention and related time-to-event endpoints.
Kaplan-Meier summaries are produced with 'tern' and 'rtables' for both
multi-arm (dose-level) and two-arm designs. Hazard ratio, Wald confidence
interval, and log-rank p-value are calculated only when exactly two
treatment arms are present. The builder can be called without launching
'shiny'.

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
