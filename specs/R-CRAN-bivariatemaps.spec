%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bivariatemaps
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Creates Bivariate Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-base 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caper 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-betapart 
BuildRequires:    R-CRAN-CommEcol 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-terra 
Requires:         R-base 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-caper 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-betapart 
Requires:         R-CRAN-CommEcol 
Requires:         R-grDevices 

%description
Contains functions mainly focused to plotting bivariate maps.

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
