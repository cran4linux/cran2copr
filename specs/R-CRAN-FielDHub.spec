%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FielDHub
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Shiny App for Design of Experiments in Life Sciences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-turner 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-blocksdesign 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-desplot 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-config 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-turner 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-blocksdesign 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-desplot 
Requires:         R-CRAN-shinyjs 

%description
A shiny design of experiments (DOE) app that aids in the creation of
traditional, un-replicated, augmented and partially-replicated designs
applied to agriculture, plant breeding, forestry, animal and biological
sciences.

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
