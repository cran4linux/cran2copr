%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SPAS
%global packver   2023.3.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2023.3.31
Release:          1%{?dist}%{?buildtag}
Summary:          Stratified-Petersen Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-TMB >= 1.7.15
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.15
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 

%description
The Stratified-Petersen Analysis System (SPAS) is designed to estimate
abundance in two-sample capture-recapture experiments where the capture
and recaptures are stratified. This is a generalization of the simple
Lincoln-Petersen estimator. Strata may be defined in time or in space or
both, and the s strata in which marking takes place may differ from the t
strata in which recoveries take place. When s=t, SPAS reduces to the
method described by Darroch (1961) <https://www.jstor.org/stable/2332748>.
When s<t, SPAS implements the methods described in Plante, Rivest, and
Tremblay (1988) <https://www.jstor.org/stable/2533994>. Schwarz and Taylor
(1998) <https://cdnsciencepub.com/doi/10.1139/f97-238> describe the use of
SPAS in estimating return of salmon stratified by time and geography. A
related package, BTSPAS, deals with temporal stratification where a spline
is used to model the distribution of the population over time as it passes
the second capture location. This is the R-version of the (now obsolete)
standalone Windows program available at
<https://home.cs.umanitoba.ca/~popan/spas/spas_home.html>.

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
