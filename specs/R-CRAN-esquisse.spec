%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  esquisse
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explore and Visualize Your Data Interactively

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-datamods >= 1.5.1
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-phosphoricons >= 0.2.1
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-downlit 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-datamods >= 1.5.1
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-shinyWidgets >= 0.6.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-phosphoricons >= 0.2.1
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-downlit 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-zip 

%description
A 'shiny' gadget to create 'ggplot2' figures interactively with
drag-and-drop to map your variables to different aesthetics. You can
quickly visualize your data accordingly to their type, export in various
formats, and retrieve the code to reproduce the plot.

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
