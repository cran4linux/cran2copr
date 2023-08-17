%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TapeR
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Tree Taper Curves Based on Semiparametric Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-nlme 
Requires:         R-splines 
Requires:         R-CRAN-pracma 

%description
Implementation of functions for fitting taper curves (a semiparametric
linear mixed effects taper model) to diameter measurements along stems.
Further functions are provided to estimate the uncertainty around the
predicted curves, to calculate timber volume (also by sections) and
marginal (e.g., upper) diameters. For cases where tree heights are not
measured, methods for estimating additional variance in volume predictions
resulting from uncertainties in tree height models (tariffs) are provided.
The example data include the taper curve parameters for Norway spruce used
in the 3rd German NFI fitted to 380 trees and a subset of section-wise
diameter measurements of these trees. The functions implemented here are
detailed in Kublin, E., Breidenbach, J., Kaendler, G. (2013)
<doi:10.1007/s10342-013-0715-0>.

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
