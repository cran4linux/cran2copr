%global packname  graticule
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Meridional and Parallel Lines for Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadmesh 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-stats 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-quadmesh 
Requires:         R-CRAN-raster 
Requires:         R-utils 
Requires:         R-CRAN-geosphere 
Requires:         R-stats 

%description
Create graticule lines and labels for maps. Control the creation of lines
by setting their placement (at particular meridians and parallels) and
extent (along parallels and meridians). Labels are created independently
of lines.

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
