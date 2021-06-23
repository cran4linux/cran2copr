%global __brp_check_rpaths %{nil}
%global packname  maptools
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Handling Spatial Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-sp >= 1.0.11
BuildRequires:    R-CRAN-foreign >= 0.8
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-sp >= 1.0.11
Requires:         R-CRAN-foreign >= 0.8
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-lattice 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Set of tools for manipulating geographic data. It includes binary access
to 'GSHHG' shoreline files. The package also provides interface wrappers
for exchanging spatial objects with packages such as 'PBSmapping',
'spatstat.geom', 'maps', and others.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
