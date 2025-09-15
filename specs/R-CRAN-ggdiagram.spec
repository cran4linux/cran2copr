%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggdiagram
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Object-Oriented Diagram Plots with 'ggplot2'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-arrowheadr 
BuildRequires:    R-CRAN-bezier 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-geomtextpath 
BuildRequires:    R-CRAN-ggarrow 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-signs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tinter 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-arrowheadr 
Requires:         R-CRAN-bezier 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-geomtextpath 
Requires:         R-CRAN-ggarrow 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggtext 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-signs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tinter 
Requires:         R-CRAN-tinytex 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
Creates diagrams with an object-oriented approach. Geometric objects have
computed properties with information about themselves (e.g., their area)
or about their relationships with other objects (e.g, the distance between
their edges). The objects have methods to convert them to geoms that can
be plotted in 'ggplot2'.

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
