%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsBase
%global packver   6.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          'DataSHIELD' Server Site Base Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-polycor >= 0.8
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-childsds 
Requires:         R-CRAN-polycor >= 0.8
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-splines 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-childsds 

%description
Base 'DataSHIELD' functions for the server side. 'DataSHIELD' is a
software package which allows you to do non-disclosive federated analysis
on sensitive data. 'DataSHIELD' analytic functions have been designed to
only share non disclosive summary statistics, with built in automated
output checking based on statistical disclosure control. With data sites
setting the threshold values for the automated output checks. For more
details, see 'citation("dsBase")'.

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
