%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggautomap
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Create Maps from a Column of Place Names

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-vctrs >= 0.4.0
BuildRequires:    R-CRAN-packcircles >= 0.3.4
BuildRequires:    R-CRAN-ggmapinset >= 0.3
BuildRequires:    R-CRAN-cartographer >= 0.2
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-vctrs >= 0.4.0
Requires:         R-CRAN-packcircles >= 0.3.4
Requires:         R-CRAN-ggmapinset >= 0.3
Requires:         R-CRAN-cartographer >= 0.2

%description
Mapping tools that convert place names to coordinates on the fly. These
'ggplot2' extensions make maps from a data frame where one of the columns
contains place names, without having to directly work with the underlying
geospatial data and tools. The corresponding map data must be registered
with 'cartographer' either by the user or by another package.

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
