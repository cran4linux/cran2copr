%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Certara.ModelResults
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Diagnostics for Pharmacometric Models Using 'shiny'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-bslib >= 0.7.0
BuildRequires:    R-CRAN-shinyTree >= 0.3.1
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinymeta 
BuildRequires:    R-CRAN-Certara.Xpose.NLME 
BuildRequires:    R-CRAN-xpose 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-bslib >= 0.7.0
Requires:         R-CRAN-shinyTree >= 0.3.1
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinymeta 
Requires:         R-CRAN-Certara.Xpose.NLME 
Requires:         R-CRAN-xpose 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-shinyjqui 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 

%description
Utilize the 'shiny' interface to generate Goodness of Fit (GOF) plots and
tables for Non-Linear Mixed Effects (NLME / NONMEM) pharmacometric models.
From the interface, users can customize model diagnostics and generate the
underlying R code to reproduce the diagnostic plots and tables outside of
the 'shiny' session. Model diagnostics can be included in a 'rmarkdown'
document and rendered to desired output format.

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
