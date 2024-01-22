%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydroGOF
%global packver   0.5-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Functions for Comparison of Simulated and Observed Hydrological Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.2
BuildRequires:    R-CRAN-xts >= 0.8.2
BuildRequires:    R-CRAN-hydroTSM >= 0.5.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-zoo >= 1.7.2
Requires:         R-CRAN-xts >= 0.8.2
Requires:         R-CRAN-hydroTSM >= 0.5.0
Requires:         R-methods 
Requires:         R-stats 

%description
S3 functions implementing both statistical and graphical goodness-of-fit
measures between observed and simulated values, mainly oriented to be used
during the calibration, validation, and application of hydrological
models. Missing values in observed and/or simulated values can be removed
before computations. Comments / questions / collaboration of any kind are
very welcomed.

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
