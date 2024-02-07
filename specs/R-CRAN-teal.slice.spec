%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.slice
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Filter Module for 'teal' Applications

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.2.2
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.2
BuildRequires:    R-CRAN-htmltools >= 0.5.4
BuildRequires:    R-CRAN-bslib >= 0.4.0
BuildRequires:    R-CRAN-teal.data >= 0.4.0
BuildRequires:    R-CRAN-teal.widgets >= 0.4.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-logger >= 0.2.0
BuildRequires:    R-CRAN-teal.logger >= 0.1.1
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-utils 
Requires:         R-CRAN-plotly >= 4.9.2.2
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-shinyWidgets >= 0.6.2
Requires:         R-CRAN-htmltools >= 0.5.4
Requires:         R-CRAN-bslib >= 0.4.0
Requires:         R-CRAN-teal.data >= 0.4.0
Requires:         R-CRAN-teal.widgets >= 0.4.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-logger >= 0.2.0
Requires:         R-CRAN-teal.logger >= 0.1.1
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-shinyjs 
Requires:         R-utils 

%description
Data filtering module for 'teal' applications.  Allows for interactive
filtering of data stored in 'data.frame' and 'MultiAssayExperiment'
objects. Also displays filtered and unfiltered observation counts.

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
