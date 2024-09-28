%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  car
%global packver   3.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Companion to Applied Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-carData >= 3.0.0
BuildRequires:    R-CRAN-lme4 >= 1.1.27.1
BuildRequires:    R-CRAN-pbkrtest >= 0.4.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-carData >= 3.0.0
Requires:         R-CRAN-lme4 >= 1.1.27.1
Requires:         R-CRAN-pbkrtest >= 0.4.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-quantreg 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-scales 

%description
Functions to Accompany J. Fox and S. Weisberg, An R Companion to Applied
Regression, Third Edition, Sage, 2019.

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
