%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  afpt
%global packver   1.1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Modelling of Animal Flight Performance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Allows estimation and modelling of flight costs in animal (vertebrate)
flight, implementing the aerodynamic power model described in Klein
Heerenbrink et al. (2015) <doi:10.1098/rspa.2014.0952>. Taking inspiration
from the program 'Flight', developed by Colin Pennycuick (Pennycuick
(2008) "Modelling the flying bird". Amsterdam: Elsevier. ISBN
0-19-857721-4), flight performance is estimated based on basic
morphological measurements such as body mass, wingspan and wing area.
'afpt' can be used to make predictions on how animals should adjust their
flight behaviour and wingbeat kinematics to varying flight conditions.

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
