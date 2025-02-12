%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polyCub
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Cubature over Polygonal Domains

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-sp >= 1.0.11
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-sp >= 1.0.11
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Numerical integration of continuously differentiable functions f(x,y) over
simple closed polygonal domains. The following cubature methods are
implemented: product Gauss cubature (Sommariva and Vianello, 2007,
<doi:10.1007/s10543-007-0131-2>), the simple two-dimensional midpoint rule
(wrapping 'spatstat.geom' functions), and adaptive cubature for radially
symmetric functions via line integrate() along the polygon boundary (Meyer
and Held, 2014, <doi:10.1214/14-AOAS743>, Supplement B). For simple
integration along the axes, the 'cubature' package is more appropriate.

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
