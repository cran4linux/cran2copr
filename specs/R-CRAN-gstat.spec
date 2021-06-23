%global __brp_check_rpaths %{nil}
%global packname  gstat
%global packver   2.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Spatio-Temporal Geostatistical Modelling, Prediction and Simulation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-spacetime >= 1.0.0
BuildRequires:    R-CRAN-sp >= 0.9.72
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-spacetime >= 1.0.0
Requires:         R-CRAN-sp >= 0.9.72
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-FNN 

%description
Variogram modelling; simple, ordinary and universal point or block
(co)kriging; spatio-temporal kriging; sequential Gaussian or indicator
(co)simulation; variogram and variogram map plotting utility functions;
supports sf and stars.

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
