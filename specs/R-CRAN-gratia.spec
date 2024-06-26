%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gratia
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Graceful 'ggplot'-Based Graphics and Other Functions for GAMs Fitted Using 'mgcv'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-mgcv >= 1.9.0
BuildRequires:    R-CRAN-patchwork >= 1.2.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ggokabeito 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-mgcv >= 1.9.0
Requires:         R-CRAN-patchwork >= 1.2.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 
Requires:         R-grid 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-grDevices 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ggokabeito 
Requires:         R-CRAN-withr 

%description
Graceful 'ggplot'-based graphics and utility functions for working with
generalized additive models (GAMs) fitted using the 'mgcv' package.
Provides a reimplementation of the plot() method for GAMs that 'mgcv'
provides, as well as 'tidyverse' compatible representations of estimated
smooths.

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
