%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adass
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Smoothing Spline (AdaSS) Estimator for the Function-on-Function Linear Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-fda 
Requires:         R-parallel 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-plot3D 

%description
Implements the adaptive smoothing spline estimator for the
function-on-function linear regression model described in Centofanti et
al. (2023) <doi:10.1007/s00180-022-01223-6>.

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
