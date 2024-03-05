%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PMEvapotranspiration
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of the Penman-Monteith Evapotranspiration using Weather Variables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The Food and Agriculture Organization-56 Penman-Monteith is one of the
important method for estimating evapotranspiration from vegetated land
areas. This package helps to calculate reference evapotranspiration using
the weather variables collected from weather station. Evapotranspiration
is the process of water transfer from the land surface to the atmosphere
through evaporation from soil and other surfaces and transpiration from
plants. The package aims to support agricultural, hydrological, and
environmental research by offering accurate and accessible reference
evapotranspiration calculation. This package has been developed using
concept of Córdova et al. (2015)<doi:10.1016/j.apm.2022.09.004> and
Debnath et al. (2015) <doi:10.1007/s40710-015-0107-1>.

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
