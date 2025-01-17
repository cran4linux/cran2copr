%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  solaR2
%global packver   0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Radiation and Photovoltaic Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-httr2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 

%description
Provides tools for calculating solar geometry, solar radiation on
horizontal and inclined planes, and simulating the performance of various
photovoltaic (PV) systems. Supports daily and intradaily irradiation data,
enabling detailed analysis of grid-connected and water-pumping PV systems,
including shading effects and solar angle calculations.

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
