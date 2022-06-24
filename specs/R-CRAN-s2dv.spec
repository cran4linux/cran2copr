%global __brp_check_rpaths %{nil}
%global packname  s2dv
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Set of Common Tools for Seasonal to Decadal Verification

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.1.1
BuildRequires:    R-CRAN-SpecsVerification >= 0.5.0
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mapproj 
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
Requires:         R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mapproj 
Requires:         R-parallel 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-easyNCDF 
Requires:         R-CRAN-easyVerification 

%description
The advanced version of package 's2dverification'. It is intended for
'seasonal to decadal' (s2d) climate forecast verification, but it can also
be used in other kinds of forecasts or general climate analysis. This
package is specially designed for the comparison between the experimental
and observational datasets. The functionality of the included functions
covers from data retrieval, data post-processing, skill scores against
observation, to visualization. Compared to 's2dverification', 's2dv' is
more compatible with the package 'startR', able to use multiple cores for
computation and handle multi-dimensional arrays with a higher flexibility.

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
