%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyMixR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive 'shiny' Dashboard for 'nlmixr2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-collapsibleTree 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-bs4Dash 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-R3port 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-fresh 
BuildRequires:    R-CRAN-nlmixr2 
BuildRequires:    R-CRAN-nlmixr2est 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-collapsibleTree 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-bs4Dash 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-R3port 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-fresh 
Requires:         R-CRAN-nlmixr2 
Requires:         R-CRAN-nlmixr2est 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cli 

%description
An R shiny user interface for the 'nlmixr2' (Fidler et al (2019)
<doi:10.1002/psp4.12445>) package, designed to simplify the modeling
process for users. Additionally, this package includes supplementary
functions to further enhances the usage of 'nlmixr2'.

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
