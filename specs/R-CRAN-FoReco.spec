%global __brp_check_rpaths %{nil}
%global packname  FoReco
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Point Forecast Reconciliation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-osqp 
Requires:         R-stats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-corpcor 
Requires:         R-methods 
Requires:         R-CRAN-mathjaxr 

%description
Classical (bottom-up and top-down), optimal and heuristic combination
forecast reconciliation procedures for cross-sectional, temporal, and
cross-temporal linearly constrained time series (Di Fonzo and Girolimetto,
2021, <doi:10.1016/j.ijforecast.2021.08.004>).

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
