%global __brp_check_rpaths %{nil}
%global packname  spotGUI
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical User Interface for the Package 'SPOT'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SPOT >= 2.0.3
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rclipboard 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-batchtools 
Requires:         R-CRAN-SPOT >= 2.0.3
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rclipboard 
Requires:         R-CRAN-plotly 
Requires:         R-tools 
Requires:         R-CRAN-httpuv 
Requires:         R-methods 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-batchtools 

%description
A graphical user interface for the Sequential Parameter Optimization
Toolbox (package 'SPOT'). It includes a quick, graphical setup for spot,
interactive 3D plots, export possibilities and more.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
