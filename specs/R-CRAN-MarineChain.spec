%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MarineChain
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blockchain-Enabled Maritime Transportation System Simulator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-plotly 

%description
Simulates Blockchain-Enabled Maritime Transportation Systems (BMTS) by
integrating asynchronous, great-circle vessel kinematics with
decentralised edge-computing consensus layers. The package provides a
fully self-contained cyber-range running completely offline, permitting
the risk-free injection of spatial and telemetry threat vectors (e.g.,
geofence breaches, coordinate modification, and node impersonation). It
includes an interactive workspace engine built using 'shinydashboard' and
'leaflet' map layers for monitoring vessel states and ledger updates.
Implemented consensus structures are modeled on a lightweight
Proof-of-Authentication framework optimized for resource-constrained
distributed nodes.

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
