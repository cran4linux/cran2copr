%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sebkc
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Surface Energy Balance and Crop Coefficient Evapotranspiration Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5
BuildRequires:    R-CRAN-sp >= 1.2
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-raster >= 2.5
Requires:         R-CRAN-sp >= 1.2
Requires:         R-CRAN-gstat 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Computes and integrates surface energy balance components of
evapotranspiration (ET), sensible heat (H), soil heat flux (G) and net
radiation (Rn) into the Food and Agriculture Organization (FAO) Irrigation
and Drainage Paper 56 (FAO-56) water balance model. The package can
perform single crop coefficient (Kc), dual Kc and the integration of
thermal-based evaporative fractions in a water balance model. The surface
energy balance models include Two-Source Surface Energy Balance (TSEB)
models, namely the Priestley-Taylor TSEB (TSEB-PT), the Penman-Monteith
TSEB (TSEB-PM) and TSEB-Parallel, as well as One-Source Surface Energy
Balance (OSEB) models, namely the Surface Energy Balance Algorithm for
Land (SEBAL), Mapping Evapotranspiration at high Resolution with
Internalized Calibration (METRIC), Surface Energy Balance Index (SEBI),
Simplified Surface Energy Balance (SSEB) and Surface Energy Balance System
(SEBS). Methods are described in Allen et al. (2007)
<doi:10.1061/(ASCE)0733-9437(2007)133:4(380)> and Bastiaanssen et al.
(1998) <doi:10.1016/S0022-1694(98)00253-4>.

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
