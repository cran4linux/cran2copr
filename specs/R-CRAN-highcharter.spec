%global __brp_check_rpaths %{nil}
%global packname  highcharter
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Wrapper for the 'Highcharts' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.1.1
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-rjson 
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.1.1
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-rjson 

%description
A wrapper for the 'Highcharts' library including shortcut functions to
plot R objects. 'Highcharts' <https://www.highcharts.com/> is a charting
library offering numerous chart types with a simple configuration syntax.

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
