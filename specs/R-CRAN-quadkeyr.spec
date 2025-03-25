%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quadkeyr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Raster Images from QuadKey-Identified Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 2.1.4
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.2
BuildRequires:    R-CRAN-sf >= 1.0.14
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-stars >= 0.6.2
Requires:         R-CRAN-readr >= 2.1.4
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-rlang >= 1.1.2
Requires:         R-CRAN-sf >= 1.0.14
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-stars >= 0.6.2

%description
A set of functions of increasing complexity allows users to (1) convert
QuadKey-identified datasets, based on 'Microsoft's Bing Maps Tile System',
into Simple Features data frames, (2) transform Simple Features data
frames into rasters, and (3) process multiple 'Meta' ('Facebook')
QuadKey-identified human mobility files directly into raster files. For
more details, see D’Andrea et al. (2024) <doi:10.21105/joss.06500>.

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
