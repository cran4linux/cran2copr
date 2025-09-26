%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  s2dv
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Seasonal to Decadal Verification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.1.1
BuildRequires:    R-CRAN-SpecsVerification >= 0.5.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ClimProjDiags 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-easyNCDF 
BuildRequires:    R-CRAN-easyVerification 
Requires:         R-CRAN-multiApply >= 2.1.1
Requires:         R-CRAN-SpecsVerification >= 0.5.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-mapproj 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-easyNCDF 
Requires:         R-CRAN-easyVerification 

%description
An advanced version of package 's2dverification'. Intended for seasonal to
decadal (s2d) climate forecast verification, but also applicable to other
types of forecasts or general climate analysis. This package is
specifically designed for comparing experimental and observational
datasets. It provides functionality for data retrieval, post-processing,
skill score computation against observations, and visualization. Compared
to 's2dverification', 's2dv' is more compatible with the package 'startR',
able to use multiple cores for computation and handle multi-dimensional
arrays with a higher flexibility. The Climate Data Operators (CDO) version
used in development is 1.9.8. Implements methods described in Wilks (2011)
<doi:10.1016/B978-0-12-385022-5.00008-7>, DelSole and Tippett (2016)
<doi:10.1175/MWR-D-15-0218.1>, Kharin et al. (2012)
<doi:10.1029/2012GL052647>, Doblas-Reyes et al. (2003)
<doi:10.1007/s00382-003-0350-4>.

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
