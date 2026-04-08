%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drhutools
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Political Science Academic Research Gears

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-png 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Using these tools to simplify the research process of political science
and other social sciences. The current version can create folder system
for academic project in political science, calculate psychological trait
scores, visualize experimental and spatial data, set up color-blind
palette, and test for Type I error (false positives) in Qualitative
Comparative Analysis (QCA) for crisp-set, multi-value, and fuzzy-set
variants.

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
