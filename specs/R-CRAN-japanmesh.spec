%global __brp_check_rpaths %{nil}
%global packname  japanmesh
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Mesh Codes in Japan

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils >= 4.2.0
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-geosphere >= 1.5.14
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-sf >= 1.0.3
BuildRequires:    R-CRAN-units >= 0.7.2
BuildRequires:    R-CRAN-rlang >= 0.4.12
BuildRequires:    R-CRAN-vctrs >= 0.3.8
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-utils >= 4.2.0
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-geosphere >= 1.5.14
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-sf >= 1.0.3
Requires:         R-CRAN-units >= 0.7.2
Requires:         R-CRAN-rlang >= 0.4.12
Requires:         R-CRAN-vctrs >= 0.3.8
Requires:         R-CRAN-purrr >= 0.3.4

%description
Functions for mesh codes in Japan. Conversion between mesh and
longitude/latitude, and between mesh codes of different scales.

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
