%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iNZightTools
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for 'iNZight'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-readr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.9
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-readr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.9
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-srvyr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
Provides a collection of wrapper functions for common variable and dataset
manipulation workflows primarily used by 'iNZight', a graphical user
interface providing easy exploration and visualisation of data for
students of statistics, available in both desktop and online versions.
Additionally, many of the functions return the 'tidyverse' code used to
obtain the result in an effort to bridge the gap between GUI and coding.

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
