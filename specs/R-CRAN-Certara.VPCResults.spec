%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Certara.VPCResults
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Visual Predictive Checks (VPC) Using 'shiny'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-bslib >= 0.7.0
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinymeta 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-tidyvpc 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-bslib >= 0.7.0
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinymeta 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-tidyvpc 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Utilize the 'shiny' interface to parameterize a Visual Predictive Check
(VPC), including selecting from different binning or binless methods and
performing stratification, censoring, and prediction correction. Generate
the underlying 'tidyvpc' and 'ggplot2' code directly from the user
interface and download R or Rmd scripts to reproduce the VPCs in R.

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
