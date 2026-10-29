%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rd2dnet
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Boundary Discontinuity Designs on Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimation and inference for boundary discontinuity designs on street
networks. Extends the location-based framework of 'rd2d' (Cattaneo,
Titiunik and Yu, <doi:10.48550/arXiv.2505.07989>) from Euclidean
coordinates to network-native coordinates (signed network distance to the
boundary and offset along it) and user-defined network metrics (edge
costs, travel time, road-class transition penalties, precomputed
matrices). Provides side-specific local polynomial estimates of boundary
average treatment effect curves with robust bias-corrected inference
(Calonico, Cattaneo and Titiunik, 2014, <doi:10.3982/ECTA11757>), uniform
confidence bands, weighted and largest aggregate effects, fuzzy designs,
covariates, derivative targets, heteroskedasticity-robust, cluster and
network Conley (1999, <doi:10.1016/S0304-4076(98)00084-0>) standard
errors, a port of the 'rd2d' direct plug-in bandwidth selector, and a
network-normalised version of the local polynomial density test of
Cattaneo, Jansson and Ma (2020, <doi:10.1080/01621459.2019.1635480>).

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
