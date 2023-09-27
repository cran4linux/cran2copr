%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R0
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of R0 and Real-Time Reproduction Number from Epidemics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Estimation of reproduction numbers for disease outbreak, based on
incidence data. The R0 package implements several documented methods. It
is therefore possible to compare estimations according to the methods
used. Depending on the methods requested by user, basic reproduction
number (commonly denoted as R0) or real-time reproduction number (referred
to as R(t)) is computed, along with a 95%% Confidence Interval. Plotting
outputs will give different graphs depending on the methods requested :
basic reproductive number estimations will only show the epidemic curve
(collected data) and an adjusted model, whereas real-time methods will
also show the R(t) variations throughout the outbreak time period.
Sensitivity analysis tools are also provided, and allow for investigating
effects of varying Generation Time distribution or time window on
estimates.

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
