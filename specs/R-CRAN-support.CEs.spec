%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  support.CEs
%global packver   0.7-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Functions for Supporting an Implementation of Choice Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-simex 
BuildRequires:    R-stats 
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-simex 
Requires:         R-stats 

%description
Provides basic functions that support an implementation of (discrete)
choice experiments (CEs). CEs is a question-based survey method measuring
people's preferences for goods/services and their characteristics. Refer
to Louviere et al. (2000) <doi:10.1017/CBO9780511753831> for details on
CEs, and Aizaki (2012) <doi:10.18637/jss.v050.c02> for the package.

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
