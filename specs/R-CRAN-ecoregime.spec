%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecoregime
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Ecological Dynamic Regimes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ecotraj >= 1.1.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ecotraj >= 1.1.1
Requires:         R-CRAN-ape 
Requires:         R-CRAN-data.table 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-smacof 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
A toolbox for implementing the Ecological Dynamic Regime framework,
including functions to characterize and compare groups of ecological
trajectories (Sánchez-Pinillos et al., 2023 <doi:10.1002/ecm.1589>);
assess the ecological resilience of a disturbed system using a reference
dynamic regime (Sánchez-Pinillos et al., 2024
<doi:10.1016/j.biocon.2023.110409>); and forecast ecological trajectories
from a dynamic regime (Sánchez-Pinillos et al. 2026,
<doi:10.1111/2041-210x.70372>). Additional functions are also available
for visualizing ecological dynamic regimes, their representative
trajectories, as well as predicted trajectories in a multidimensional
state space.

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
