%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  basifoR
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieval and Processing of the Spanish National Forest Inventory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-measurements 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-measurements 
Requires:         R-stats 
Requires:         R-utils 

%description
Data sets of the Spanish National Forest Inventory
<https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/informacion-disponible.html>
are processed to compute tree metrics and statistics. Function
metrics2Vol() controls most of the routines.

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
