%global __brp_check_rpaths %{nil}
%global packname  strm
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Regression Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 3.0.2
BuildRequires:    R-CRAN-rmarkdown >= 2.6
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-rgdal >= 1.5.23
BuildRequires:    R-CRAN-knitr >= 1.33
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-spatialreg >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-testthat >= 3.0.2
Requires:         R-CRAN-rmarkdown >= 2.6
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-rgdal >= 1.5.23
Requires:         R-CRAN-knitr >= 1.33
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-spatialreg >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-utils 

%description
Implements a spatio-temporal regression model based on Chi, G. and Zhu, J.
(2019) Spatial Regression Models for the Social Sciences
<isbn:9781544302072>. The approach here fits a spatial error model while
incorporating a temporally lagged response variable and temporally lagged
explanatory variables. This package builds on the errorsarlm() function
from the spatialreg package.

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
