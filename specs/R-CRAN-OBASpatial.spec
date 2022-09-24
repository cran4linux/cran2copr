%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OBASpatial
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Objective Bayesian Analysis for Spatial Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-modeest 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-modeest 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-mvtnorm 

%description
It makes an objective Bayesian analysis of the spatial regression model
using both the normal (NSR) and student-T (TSR) distributions. The
functions provided give prior and posterior objective densities and allow
default Bayesian estimation of the model regression parameters. Details
can be found in Ordonez et al. (2020) <arXiv:2004.04341>.

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
