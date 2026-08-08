%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  libcmaesr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'libcmaes'

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-mlr3misc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-mlr3misc 
Requires:         R-stats 

%description
A lightweight interface to the 'libcmaes' C++ library for the Covariance
Matrix Adaptation Evolution Strategy (CMA-ES). CMA-ES is a
state-of-the-art evolutionary algorithm for the optimization of difficult
non-linear, non-convex black-box functions, as described in Hansen and
Ostermeier (2001) <doi:10.1162/106365601750190398>. Supports the active,
separable, and VD (diagonal plus rank-one covariance) variants of the
algorithm as well as the IPOP (increasing population size) and BIPOP
(bi-population) restart strategies. A patched copy of 'libcmaes' (LGPL >=
3) is bundled; see the COPYRIGHTS file for details.

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
