%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FoReco
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forecast Reconciliation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-osqp 
Requires:         R-stats 
Requires:         R-CRAN-cli 

%description
Classical (bottom-up and top-down), optimal combination and heuristic
point (Di Fonzo and Girolimetto, 2023
<doi:10.1016/j.ijforecast.2021.08.004>) and probabilistic (Girolimetto et
al. 2024 <doi:10.1016/j.ijforecast.2023.10.003>) forecast reconciliation
procedures for linearly constrained time series (e.g., hierarchical or
grouped time series) in cross-sectional, temporal, or cross-temporal
frameworks.

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
