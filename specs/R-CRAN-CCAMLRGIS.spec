%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CCAMLRGIS
%global packver   4.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Antarctic Spatial Data Manipulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-isoband 
BuildRequires:    R-CRAN-bezier 
BuildRequires:    R-CRAN-lwgeom 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-terra 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-isoband 
Requires:         R-CRAN-bezier 
Requires:         R-CRAN-lwgeom 

%description
Loads and creates spatial data, including layers and tools that are
relevant to the activities of the Commission for the Conservation of
Antarctic Marine Living Resources. Provides two categories of functions:
load functions and create functions. Load functions are used to import
existing spatial layers from the online CCAMLR GIS such as the ASD
boundaries. Create functions are used to create layers from user data such
as polygons and grids.

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
