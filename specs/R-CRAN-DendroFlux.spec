%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DendroFlux
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Processing and Analyzing Dendrometer and Sap Flux Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-rlang 

%description
Data management and cleaning for dendrometer and sap flux data, including
gap detection, NA identification, missing value interpolation, and date
conversion. The package also calculates multiple growth metrics of tree
radial change data, including the cumulative growth over the entire
observation period, daily cumulative growth, and growth changes between
adjacent time intervals. Various approaches can be applied to calculate
the night delta-Tmax required for sap flow (Peters et al., 2018, <doi:
10.1111/nph.15241>) and subsequently estimate sap flow density (Granier,
1987, <doi: 10.1093/treephys/3.4.309>). In addition, it supports the
creation of simple time‑series point plots to visually display the dynamic
changes in tree growth status or sap flow density during that period.

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
