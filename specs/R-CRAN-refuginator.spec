%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refuginator
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          An Interactive Tool for Identifying Refugia

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-neotoma2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-rnaturalearthdata 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-neotoma2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-rnaturalearthdata 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 

%description
A 'shiny'-based browser application for reconstructing organismal
distributions and identifying historical and geohistorical refugia using
the methods published by Morley et al. (2026)
<doi:10.1038/s43247-026-03563-3>.

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
