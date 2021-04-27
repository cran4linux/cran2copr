%global packname  rerddapXtracto
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extracts Environmental Data from 'ERDDAP' Web Services

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rerddap >= 0.6.0
BuildRequires:    R-CRAN-plotdap >= 0.0.5
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rerddap >= 0.6.0
Requires:         R-CRAN-plotdap >= 0.0.5
Requires:         R-CRAN-abind 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains three functions that access environmental data from any 'ERDDAP'
data web service. The rxtracto() function extracts data along a trajectory
for a given "radius" around the point. The rxtracto_3D() function extracts
data in a box. The rxtractogon() function extracts data in a polygon. All
of those three function use the 'rerddap' package to extract the data, and
should work with any 'ERDDAP' server. There are also two functions,
plotBBox() and plotTrack() that use the 'plotdap' package to simplify the
creation of maps of the data.

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
