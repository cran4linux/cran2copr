%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyquant
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Quantitative Financial Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-timetk >= 2.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-quantmod >= 0.4.13
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-RobStatTM 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-timetk >= 2.4.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-quantmod >= 0.4.13
Requires:         R-CRAN-httr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-RobStatTM 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-cli 

%description
Bringing business and financial analysis to the 'tidyverse'. The
'tidyquant' package provides a convenient wrapper to various 'xts', 'zoo',
'quantmod', 'TTR' and 'PerformanceAnalytics' package functions and returns
the objects in the tidy 'tibble' format. The main advantage is being able
to use quantitative functions with the 'tidyverse' functions including
'purrr', 'dplyr', 'tidyr', 'ggplot2', 'lubridate', etc. See the
'tidyquant' website for more information, documentation and examples.

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
