%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecotraj
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Trajectory Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-MASS 

%description
Analysis of temporal changes (i.e. dynamics) of ecological entities,
defined as trajectories on a chosen multivariate space, by providing a set
of trajectory metrics and visual representations [De Caceres et al. (2019)
<doi:10.1002/ecm.1350>; and Sturbois et al. (2021)
<doi:10.1016/j.ecolmodel.2020.109400>]. Includes functions to estimate
metrics for individual trajectories (length, directionality, angles, ...)
as well as metrics to relate pairs of trajectories (dissimilarity and
convergence). Functions are also provided to estimate the ecological
quality of ecosystem with respect to reference conditions [Sturbois et al.
(2023) <doi:10.1002/ecs2.4726>].

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
