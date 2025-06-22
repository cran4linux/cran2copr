%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geosptdb
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Radial Basis Functions with Distance-Based Methods (Optimization, Prediction and Cross Validation)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-geospt 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-StatMatch 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-geospt 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Spatio-temporal radial basis functions (optimization, prediction and
cross-validation), summary statistics from cross-validation, Adjusting
distance-based linear regression model and generation of the principal
coordinates of a new individual from Gower's distance.

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
