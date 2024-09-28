%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  normfluodbf
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cleans and Normalizes FLUOstar DBF and DAT Files from 'Liposome' Flux Assays

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.4
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-testthat >= 3.2.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-foreign >= 0.8.86
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-emojifont 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-badger 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-pkgsearch 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-wesanderson 
BuildRequires:    R-CRAN-hexSticker 
Requires:         R-CRAN-plotly >= 4.10.4
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-testthat >= 3.2.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-foreign >= 0.8.86
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-emojifont 
Requires:         R-stats 
Requires:         R-CRAN-badger 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-pkgsearch 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-wesanderson 
Requires:         R-CRAN-hexSticker 

%description
Cleans and Normalizes FLUOstar DBF and DAT Files obtained from liposome
flux assays. Users should verify extended usage of the package on files
from other assay types.

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
