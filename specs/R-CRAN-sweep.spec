%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sweep
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Tools for Forecasting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.0
BuildRequires:    R-CRAN-timetk >= 2.1.0
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-broom >= 0.5.6
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-forecast >= 8.0
Requires:         R-CRAN-timetk >= 2.1.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-broom >= 0.5.6
Requires:         R-CRAN-rlang 

%description
Tidies up the forecasting modeling and prediction work flow, extends the
'broom' package with 'sw_tidy', 'sw_glance', 'sw_augment', and
'sw_tidy_decomp' functions for various forecasting models, and enables
converting 'forecast' objects to "tidy" data frames with 'sw_sweep'.

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
