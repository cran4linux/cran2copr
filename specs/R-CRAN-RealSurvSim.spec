%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RealSurvSim
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Survival Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-kdensity 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-univariateML 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FAdist 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-kdensity 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-univariateML 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-flexsurv 
Requires:         R-stats 
Requires:         R-CRAN-FAdist 

%description
Provides tools for simulating synthetic survival data using a variety of
methods, including kernel density estimation, parametric distribution
fitting, and bootstrap resampling techniques for a desired sample size.

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
