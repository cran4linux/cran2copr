%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RNCEP
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Obtain, Organize, and Visualize NCEP Weather Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-tcltk 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-tgp 
Requires:         R-tcltk 
Requires:         R-graphics 
Requires:         R-CRAN-sp 

%description
Contains functions to retrieve, organize, and visualize weather data from
the NCEP/NCAR Reanalysis
(<https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html>) and
NCEP/DOE Reanalysis II
(<https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html>) datasets.
Data are queried via the Internet and may be obtained for a specified
spatial and temporal extent or interpolated to a point in space and time.
We also provide functions to visualize these weather data on a map.  There
are also functions to simulate flight trajectories according to specified
behavior using either NCEP wind data or data specified by the user.

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
