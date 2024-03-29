%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthyverse
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'healthyverse'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-healthyR 
BuildRequires:    R-CRAN-healthyR.data 
BuildRequires:    R-CRAN-healthyR.ts 
BuildRequires:    R-CRAN-healthyR.ai 
BuildRequires:    R-CRAN-TidyDensity 
BuildRequires:    R-CRAN-tidyAML 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-healthyR 
Requires:         R-CRAN-healthyR.data 
Requires:         R-CRAN-healthyR.ts 
Requires:         R-CRAN-healthyR.ai 
Requires:         R-CRAN-TidyDensity 
Requires:         R-CRAN-tidyAML 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-cli 

%description
The 'healthyverse' is a set of packages that work in harmony because they
share common data representations and 'API' design. This package is
designed to make it easy to install and load multiple 'healthyverse'
packages in a single step.

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
