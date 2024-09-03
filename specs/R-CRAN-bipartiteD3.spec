%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bipartiteD3
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Bipartite Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.4
BuildRequires:    R-CRAN-stringr >= 1.3
BuildRequires:    R-CRAN-RColorBrewer >= 1.1
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-r2d3 >= 0.2.2
Requires:         R-CRAN-tibble >= 1.4
Requires:         R-CRAN-stringr >= 1.3
Requires:         R-CRAN-RColorBrewer >= 1.1
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-r2d3 >= 0.2.2

%description
Generates interactive bipartite graphs using the D3 library. Designed for
use with the 'bipartite' analysis package. Includes open source 'viz-js'
library Adapted from examples at <https://bl.ocks.org/NPashaP> (released
under GPL-3).

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
