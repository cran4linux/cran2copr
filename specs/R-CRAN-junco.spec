%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  junco
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Create Common Tables and Listings Used in Clinical Trials

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-rbmi >= 1.6.0
BuildRequires:    R-CRAN-tern >= 0.9.10
BuildRequires:    R-CRAN-flextable >= 0.9.10
BuildRequires:    R-CRAN-vcdExtra >= 0.8.7
BuildRequires:    R-CRAN-rtables >= 0.6.15
BuildRequires:    R-CRAN-formatters >= 0.5.12
BuildRequires:    R-CRAN-rlistings >= 0.2.13
BuildRequires:    R-CRAN-tidytlg >= 0.11.0
BuildRequires:    R-CRAN-rtables.officer >= 0.1.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-mmrm 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-systemfonts 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-rbmi >= 1.6.0
Requires:         R-CRAN-tern >= 0.9.10
Requires:         R-CRAN-flextable >= 0.9.10
Requires:         R-CRAN-vcdExtra >= 0.8.7
Requires:         R-CRAN-rtables >= 0.6.15
Requires:         R-CRAN-formatters >= 0.5.12
Requires:         R-CRAN-rlistings >= 0.2.13
Requires:         R-CRAN-tidytlg >= 0.11.0
Requires:         R-CRAN-rtables.officer >= 0.1.0
Requires:         R-CRAN-broom 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-mmrm 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-systemfonts 

%description
Structure and formatting requirements for clinical trial table and listing
outputs vary between pharmaceutical companies. 'junco' provides additional
tooling for use alongside the 'rtables', 'rlistings' and 'tern' packages
when creating table and listing outputs. While motivated by the specifics
of Johnson and Johnson Clinical and Statistical Programming's table and
listing shells, 'junco' provides functionality that is general and
reusable. Major features include a) alternative and extended statistical
analyses beyond what 'tern' supports for use in standard safety and
efficacy tables, b) a robust production-grade Rich Text Format (RTF)
exporter for both tables and listings, c) structural support for spanning
column headers and risk difference columns in tables, and d) robust
font-aware automatic column width algorithms for both listings and tables.

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
