%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  a11yShiny
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Accessibility Enhancements to Popular R Shiny Functions

License:          EUPL-1.2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.9.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-shiny >= 1.9.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Accessible wrappers for popular 'shiny' UI components, enforcing ARIA
attributes and structural requirements in line with BITV 2.0
(Barrierefreie-Informationstechnik-Verordnung) and WCAG 2.1 AA. Covers
action buttons, text and select inputs, fluid page layouts with HTML
landmarks and skip links, 'DT' data tables, and bar and line graphs from
'ggplot2'. Components validate label presence, expose keyboard-accessible
ARIA states, and provide a high-contrast toggle. This package was
developed by d-fine GmbH on behalf of the German Federal Ministry of
Research, Technology and Space (BMFTR).

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
