%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatstat.gui
%global packver   3.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Graphics Functions for the 'spatstat' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.random >= 3.0.0
BuildRequires:    R-CRAN-spatstat.geom >= 3.0
BuildRequires:    R-CRAN-spatstat.model >= 3.0
BuildRequires:    R-CRAN-spatstat.linnet >= 3.0
BuildRequires:    R-CRAN-spatstat.data >= 3.0
BuildRequires:    R-CRAN-spatstat >= 3.0
BuildRequires:    R-CRAN-spatstat.utils >= 3.0
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-rpanel 
BuildRequires:    R-tcltk 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-spatstat.random >= 3.0.0
Requires:         R-CRAN-spatstat.geom >= 3.0
Requires:         R-CRAN-spatstat.model >= 3.0
Requires:         R-CRAN-spatstat.linnet >= 3.0
Requires:         R-CRAN-spatstat.data >= 3.0
Requires:         R-CRAN-spatstat >= 3.0
Requires:         R-CRAN-spatstat.utils >= 3.0
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-rpanel 
Requires:         R-tcltk 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 

%description
Extension to the 'spatstat' package, containing interactive graphics
capabilities.

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
