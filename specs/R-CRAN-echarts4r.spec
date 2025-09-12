%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  echarts4r
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Graphs with 'Echarts JavaScript' Version 5

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rstudioapi 

%description
Easily create interactive charts by leveraging the 'Echarts Javascript'
library which includes 36 chart types, themes, 'Shiny' proxies and
animations.

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
