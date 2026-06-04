%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ViewR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Interactive Data Tables and Data Explorer

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.6.0
BuildRequires:    R-CRAN-shinythemes >= 1.2.0
BuildRequires:    R-CRAN-htmltools >= 0.5.4
BuildRequires:    R-CRAN-rhandsontable >= 0.3.8
BuildRequires:    R-CRAN-DT >= 0.27
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-htmlwidgets >= 1.6.0
Requires:         R-CRAN-shinythemes >= 1.2.0
Requires:         R-CRAN-htmltools >= 0.5.4
Requires:         R-CRAN-rhandsontable >= 0.3.8
Requires:         R-CRAN-DT >= 0.27
Requires:         R-stats 
Requires:         R-utils 

%description
An advanced, interactive data table and data explorer for R, delivered as
a modern, self-contained 'htmlwidget' with a high-performance virtualized
grid. ViewR renders 'Kaggle'-style micro-dashboard column headers complete
with data-type badges, mini distribution spark-histograms, and
data-completeness (missingness) bars. It provides hover metadata cards, a
sliding Data Insights drawer with interactive histograms and 'Pareto'
category charts, a multi-condition visual query builder (AND/OR), a column
visibility picker, and a reproducible code generator that emits 'dplyr',
base R, and 'SQL' that matches the active filter and column state. The
interface is implemented entirely in dependency-free vanilla 'JavaScript'
(no 'React' or build toolchain) and works in the 'RStudio'/'Positron'
Viewer, inside 'Shiny' apps, in 'R Markdown'/'Quarto', or as a portable
standalone 'HTML' file. A single call to viewr() opens the explorer; the
legacy 'Shiny'-gadget ViewR() editor remains available.

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
