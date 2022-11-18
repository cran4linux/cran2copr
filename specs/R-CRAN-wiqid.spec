%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wiqid
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quick and Dirty Estimates for Wildlife Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-mcmcOutput 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-mcmcOutput 
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-plotrix 

%description
Provides simple, fast functions for maximum likelihood and Bayesian
estimates of wildlife population parameters, suitable for use with
simulated data or bootstraps. Early versions were indeed quick and dirty,
but optional error-checking routines and meaningful error messages have
been added. Includes single and multi-season occupancy, closed capture
population estimation, survival, species richness and distance measures.

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
