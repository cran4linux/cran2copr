%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthyverse
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'healthyverse'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-crayon >= 1.5.3
BuildRequires:    R-CRAN-TidyDensity >= 1.5.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-healthyR.data >= 1.1.1
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-healthyR.ts >= 0.3.0
BuildRequires:    R-CRAN-healthyR >= 0.2.2
BuildRequires:    R-CRAN-rstudioapi >= 0.16.0
BuildRequires:    R-CRAN-healthyR.ai >= 0.1.0
BuildRequires:    R-CRAN-RandomWalker >= 0.1.0
BuildRequires:    R-CRAN-tidyAML >= 0.0.5
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-crayon >= 1.5.3
Requires:         R-CRAN-TidyDensity >= 1.5.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-healthyR.data >= 1.1.1
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-healthyR.ts >= 0.3.0
Requires:         R-CRAN-healthyR >= 0.2.2
Requires:         R-CRAN-rstudioapi >= 0.16.0
Requires:         R-CRAN-healthyR.ai >= 0.1.0
Requires:         R-CRAN-RandomWalker >= 0.1.0
Requires:         R-CRAN-tidyAML >= 0.0.5

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
