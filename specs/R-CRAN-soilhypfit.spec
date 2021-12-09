%global __brp_check_rpaths %{nil}
%global packname  soilhypfit
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling of Soil Water Retention and Hydraulic Conductivity Data

License:          GPL (>= 2) | LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog >= 1.5.7
BuildRequires:    R-CRAN-nloptr >= 1.2.1
BuildRequires:    R-CRAN-Rmpfr >= 0.7.2
BuildRequires:    R-CRAN-SoilHyP >= 0.1.3
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-parallel 
Requires:         R-CRAN-quadprog >= 1.5.7
Requires:         R-CRAN-nloptr >= 1.2.1
Requires:         R-CRAN-Rmpfr >= 0.7.2
Requires:         R-CRAN-SoilHyP >= 0.1.3
Requires:         R-graphics 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mgcv 
Requires:         R-parallel 

%description
Provides functions for efficiently estimating properties of the Van
Genuchten-Mualem model for soil hydraulic parameters from possibly sparse
soil water retention and hydraulic conductivity data by multi-response
parameter estimation methods (Stewart, W.E., Caracotsios, M. Soerensen,
J.P. (1992) "Parameter estimation from multi-response data"
<doi:10.1002/aic.690380502>). Parameter estimation is simplified by
exploiting the fact that residual and saturated water contents and
saturated conductivity are conditionally linear parameters (Bates, D. M.
and Watts, D. G. (1988) "Nonlinear Regression Analysis and Its
Applications" <doi:10.1002/9780470316757>). Estimated parameters are
optionally constrained by the evaporation characteristic length (Lehmann,
P., Bickel, S., Wei, Z. and Or, D. (2020) "Physical Constraints for
Improved Soil Hydraulic Parameter Estimation by Pedotransfer Functions"
<doi:10.1029/2019WR025963>) to ensure that the estimated parameters are
physically valid.

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
