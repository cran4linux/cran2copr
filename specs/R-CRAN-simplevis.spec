%global __brp_check_rpaths %{nil}
%global packname  simplevis
%global packver   4.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simple 'ggplot2' Visualisation with Less Brainpower

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-kimisc 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-leafpop 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-DT 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-kimisc 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-leafpop 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-viridis 

%description
Wrapper functions to make 'ggplot2' and 'leaflet' visualisation easier
with less brainpower required.

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
