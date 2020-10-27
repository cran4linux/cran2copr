%global packname  sugarbag
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Create Tessellated Hexagon Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-geosphere >= 1.5
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-utf8 >= 1.1.4
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-rmapshaper >= 0.4.4
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-lwgeom >= 0.2
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-geosphere >= 1.5
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-utf8 >= 1.1.4
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 0.9
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-rmapshaper >= 0.4.4
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-lwgeom >= 0.2

%description
Create a hexagon tile map display from spatial polygons. Each polygon is
represented by a hexagon tile, placed as close to it's original centroid
as possible, with a focus on maintaining spatial relationship to a focal
point. Developed to aid visualisation and analysis of spatial
distributions across Australia, which can be challenging due to the
concentration of the population on the coast and wide open interior.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
