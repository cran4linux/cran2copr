%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ViewR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Data Viewer, Filter, and Editor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-shinythemes >= 1.2.0
BuildRequires:    R-CRAN-htmltools >= 0.5.4
BuildRequires:    R-CRAN-rhandsontable >= 0.3.8
BuildRequires:    R-CRAN-DT >= 0.27
BuildRequires:    R-utils 
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-shinythemes >= 1.2.0
Requires:         R-CRAN-htmltools >= 0.5.4
Requires:         R-CRAN-rhandsontable >= 0.3.8
Requires:         R-CRAN-DT >= 0.27
Requires:         R-utils 

%description
Provides a feature-rich, popup-based interactive interface for viewing,
exploring, filtering, sorting, editing, analysing, and plotting R data
frames. Key features include: a searchable, paginated data table with
drag-and-drop column reordering and variable-label 'tooltips';
multi-condition filters (AND/OR) with live preview; multi-column sorting;
column visibility management with search; an Excel-like cell editor
powered by 'rhandsontable'; find-and-replace across one or all columns
(literal or regex) with automatic live preview; a Plots tab with
auto-detected histograms and bar charts for every column; automatic
'dplyr' code generation reflecting every operation performed in the 'UI';
one-click CSV export; and a Variable Info tab with type, missing values,
and summary statistics. The entire interface is launched with a single
call to ViewR() and works as a popup dialog, in the 'RStudio' Viewer pane,
or in the system browser.

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
