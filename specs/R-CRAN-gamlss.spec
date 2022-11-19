%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gamlss
%global packver   5.4-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.4.10
Release:          1%{?dist}%{?buildtag}
Summary:          Generalised Additive Models for Location Scale and Shape

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-gamlss.data >= 5.0.0
BuildRequires:    R-CRAN-gamlss.dist >= 4.3.1
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss.data >= 5.0.0
Requires:         R-CRAN-gamlss.dist >= 4.3.1
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-survival 
Requires:         R-methods 

%description
Functions for fitting the Generalized Additive Models for Location Scale
and Shape introduced by Rigby and Stasinopoulos (2005),
<doi:10.1111/j.1467-9876.2005.00510.x>. The models use a distributional
regression approach where all the parameters of the conditional
distribution of the response variable are modelled using explanatory
variables.

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
