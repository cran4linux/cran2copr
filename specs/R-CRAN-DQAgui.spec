%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DQAgui
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical User Interface for Data Quality Assessment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DIZtools >= 1.0.1
BuildRequires:    R-CRAN-DQAstats >= 0.3.5
BuildRequires:    R-CRAN-DIZutils >= 0.1.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-daterangepicker 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-waiter 
Requires:         R-CRAN-DIZtools >= 1.0.1
Requires:         R-CRAN-DQAstats >= 0.3.5
Requires:         R-CRAN-DIZutils >= 0.1.2
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-daterangepicker 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-utils 
Requires:         R-CRAN-waiter 

%description
A graphical user interface (GUI) to the functions implemented in the R
package 'DQAstats'. Publication: Mang et al. (2021)
<doi:10.1186/s12911-022-01961-z>.

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
