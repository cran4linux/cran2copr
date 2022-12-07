%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydraulics
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Pipe and Open Channel Hydraulics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-units 

%description
Functions for basic hydraulic calculations related to water flow in
circular pipes both flowing full (under pressure), and partially full
(gravity flow), and trapezoidal open channels. For pressure flow this
includes friction loss calculations by solving the Darcy-Weisbach equation
for head loss, flow or diameter, plotting a Moody diagram, matching a pump
characteristic curve to a system curve, and solving for flows in a pipe
network using the Hardy-Cross method. The Darcy-Weisbach friction factor
is calculated using the Colebrook (or Colebrook-White equation), the basis
of the Moody diagram, the original citation being Colebrook (1939)
<doi:10.1680/ijoti.1939.13150>. For gravity flow, the Manning equation is
used, again solving for missing parameters. The derivation of and
solutions using the Darcy-Weisbach equation and the Manning equation are
outlined in many fluid mechanics texts such as Finnemore and Franzini
(2002, ISBN:978-0072432022). Some gradually- and rapidly-varied flow
functions are included. For the Manning equation solutions, this package
uses modifications of original code from the 'iemisc' package by Irucka
Embry.

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
