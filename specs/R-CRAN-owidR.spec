%global __brp_check_rpaths %{nil}
%global packname  owidR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Package for Importing Data from Our World in Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-grDevices 

%description
Imports data from the Our World in Data website, offering easy to use
functions for searching for datasets, downloading them into R and
visualising them.

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
