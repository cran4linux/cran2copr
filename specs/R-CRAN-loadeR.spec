%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  loadeR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Load Data for Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-echarts4r 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycustomloader 
Requires:         R-CRAN-shinydashboardPlus >= 2.0.0
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-DT 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-config 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-echarts4r 
Requires:         R-grDevices 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycustomloader 

%description
Provides a framework to load text and excel files through a 'shiny'
graphical interface. It allows renaming, transforming, ordering and
removing variables. It includes basic exploratory methods such as the
mean, median, mode, normality test, histogram and correlation.

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
