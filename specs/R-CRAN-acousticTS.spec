%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  acousticTS
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Physics-Based Models for Acoustic Target Strength

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Acoustic target strength (TS) represents the intensity of an echo
returning from an individual scatterer such as bubbles, fish, or
zooplankton. TS can be used to convert integrated or volumetric
backscatter collected from fisheries acoustic surveys into units of number
density (e.g. animals per m^3), abundance (e.g. number of animals), and
biomass (e.g. kg). This parameter can also be used to aid in classifying
backscatter, such as separating likely echoes of large predatory fish
(e.g. adult cod) from smaller prey (e.g. shrimp). One way to estimate TS
is to use physics-based models to calculate theoretical TS that comprise
exact and approximate solutions as well as analytical approaches. The
models provided can help provide TS estimates over broad statistical
distributions of model parameters. Applications are described by Lucca et
al. (2023) <doi:10.1121/10.0022459>, with fisheries-acoustics principles
from Simmonds and MacLennan (2005) <doi:10.1002/9780470995303>.

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
