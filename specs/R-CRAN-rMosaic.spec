%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rMosaic
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Bindings to the 'Mosaic' Visualization Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.3.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.4
BuildRequires:    R-CRAN-duckdb >= 1.4.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-stats 
Requires:         R-CRAN-yaml >= 2.3.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-htmlwidgets >= 1.5.4
Requires:         R-CRAN-duckdb >= 1.4.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-stats 

%description
Provides R bindings for 'Mosaic', a declarative grammar for linked,
data-driven visualizations backed by 'DuckDB'. The package supplies
'htmlwidgets' and 'shiny' helpers for rendering 'Mosaic' specifications
from R, including optional browser-side 'DuckDB-WASM' execution and
selection export helpers for exploratory workflows.

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
