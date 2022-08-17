%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nbody
%global packver   1.33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.33
Release:          1%{?dist}%{?buildtag}
Summary:          Gravitational N-Body Simulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-magicaxis 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-magicaxis 

%description
Tools to run simple direct gravitational N-body simulations. It can access
different external N-body simulators, but also has a simple built-in
default simulator. This default simulator uses a variable block time step
and lets the user choose between a range of integrators, including 4th and
6th order integrators for high-accuracy simulations. Basic top-hat
smoothing is available as an option. The code also allows the definition
of background particles that are fixed or in uniform motion, not subject
to acceleration by other particles.

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
