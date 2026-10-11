%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EZRShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build Consistent 'shiny' App Layouts with Less Code

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.12.0
BuildRequires:    R-CRAN-shiny >= 1.8.0
BuildRequires:    R-CRAN-ggiraph >= 0.9.1
BuildRequires:    R-CRAN-bslib >= 0.7.0
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-utils 
Requires:         R-CRAN-plotly >= 4.12.0
Requires:         R-CRAN-shiny >= 1.8.0
Requires:         R-CRAN-ggiraph >= 0.9.1
Requires:         R-CRAN-bslib >= 0.7.0
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-here 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-utils 

%description
Short, consistent wrappers around 'shiny', 'bslib' and 'shinyjs' for
building multi-page 'shiny' apps. One function call builds the page with a
navigation bar, logo, title and dark mode switch. Tab functions nest pages
up to three levels deep, with optional sidebars. Input functions create
full-width inputs with optional information tooltips, and helpers switch
buttons on and off and show or hide tabs from the server. Includes a
starter app template and an example app that explores the Titanic
passenger data.

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
