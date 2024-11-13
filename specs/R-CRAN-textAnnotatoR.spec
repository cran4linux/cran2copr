%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  textAnnotatoR
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Text Annotation Tool with 'shiny' GUI

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-readtext 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-readtext 
Requires:         R-CRAN-magrittr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
A comprehensive text annotation tool built with 'shiny'. Provides an
interactive graphical user interface for coding text documents, managing
code hierarchies, creating memos, and analyzing coding patterns. Features
include code co-occurrence analysis, visualization of coding patterns,
comparison of multiple coding sets, and export capabilities. Supports
collaborative qualitative research through standardized annotation formats
and analysis tools.

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
