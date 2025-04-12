%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coarseDataTools
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Coarsely Observed Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-MCMCpack 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Functions to analyze coarse data. Specifically, it contains functions to
(1) fit parametric accelerated failure time models to interval-censored
survival time data, and (2) estimate the case-fatality ratio in scenarios
with under-reporting. This package's development was motivated by
applications to infectious disease: in particular, problems with
estimating the incubation period and the case fatality ratio of a given
disease.  Sample data files are included in the package. See Reich et al.
(2009) <doi:10.1002/sim.3659>, Reich et al. (2012)
<doi:10.1111/j.1541-0420.2011.01709.x>, and Lessler et al. (2009)
<doi:10.1016/S1473-3099(09)70069-6>.

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
