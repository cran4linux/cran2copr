%global __brp_check_rpaths %{nil}
%global packname  rassta
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Raster-Based Spatial Stratification Algorithms

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.4.1
BuildRequires:    R-grDevices >= 4.1.0
BuildRequires:    R-stats >= 4.1.0
BuildRequires:    R-utils >= 4.1.0
BuildRequires:    R-CRAN-raster >= 3.4.13
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-kohonen >= 3.0.10
BuildRequires:    R-CRAN-KernSmooth >= 2.23.18
BuildRequires:    R-CRAN-cluster >= 2.1.2
BuildRequires:    R-CRAN-GGally >= 2.1.2
BuildRequires:    R-CRAN-stringi >= 1.7.2
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-terra >= 1.3.4
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-stringdist >= 0.9.6.3
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-DT >= 0.18
BuildRequires:    R-CRAN-histogram >= 0.0.25
Requires:         R-CRAN-plotly >= 4.9.4.1
Requires:         R-grDevices >= 4.1.0
Requires:         R-stats >= 4.1.0
Requires:         R-utils >= 4.1.0
Requires:         R-CRAN-raster >= 3.4.13
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-kohonen >= 3.0.10
Requires:         R-CRAN-KernSmooth >= 2.23.18
Requires:         R-CRAN-cluster >= 2.1.2
Requires:         R-CRAN-GGally >= 2.1.2
Requires:         R-CRAN-stringi >= 1.7.2
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-terra >= 1.3.4
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-stringdist >= 0.9.6.3
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-DT >= 0.18
Requires:         R-CRAN-histogram >= 0.0.25

%description
Algorithms for the spatial stratification of landscapes, sampling and
modeling of spatially-varying phenomena. These algorithms offer a simple
framework for the stratification of geographic space based on raster
layers representing landscape factors and/or factor scales. The
stratification process follows a hierarchical approach, which is based on
first level units (i.e., classification units) and second-level units
(i.e., stratification units). Nonparametric techniques allow to measure
the correspondence between the geographic space and the landscape
configuration represented by the units. These correspondence metrics are
useful to define sampling schemes and to model the spatial variability of
environmental phenomena.

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
