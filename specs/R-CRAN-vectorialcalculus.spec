%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vectorialcalculus
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Vector Calculus Tools for Visualization and Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides pedagogical tools for visualization and numerical computation in
vector calculus. Includes functions for parametric curves, scalar and
vector fields, gradients, divergences, curls, line and surface integrals,
and dynamic 2D/3D graphical analysis to support teaching and learning. The
implemented methods follow standard treatments in vector calculus and
multivariable analysis as presented in Marsden and Tromba (2011)
<ISBN:9781429215084>, Stewart (2015) <ISBN:9781285741550>, Thomas, Weir
and Hass (2018) <ISBN:9780134438986>, Larson and Edwards (2016)
<ISBN:9781285255869>, Apostol (1969) <ISBN:9780471000051>, Spivak (1971)
<ISBN:9780805390216>, Schey (2005) <ISBN:9780071369080>, Colley (2019)
<ISBN:9780321982384>, Lizarazo Osorio (2020) <ISBN:9789585450103>, Sievert
(2020) <ISBN:9780367180165>, and Borowko (2013) <ISBN:9781439870791>.

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
