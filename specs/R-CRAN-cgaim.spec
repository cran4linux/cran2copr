%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cgaim
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Groupwise Additive Index Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-scar 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cgam 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-gratia 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-CRAN-TruncatedNormal 
BuildRequires:    R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-scar 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-Matrix 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cgam 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-gratia 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-coneproj 
Requires:         R-CRAN-TruncatedNormal 
Requires:         R-CRAN-foreach 

%description
Fits constrained groupwise additive index models and provides functions
for inference and interpretation of these models. The method is described
in Masselot, Chebana, Campagna, Lavigne, Ouarda, Gosselin (2022)
"Constrained groupwise additive index models"
<doi:10.1093/biostatistics/kxac023>.

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
