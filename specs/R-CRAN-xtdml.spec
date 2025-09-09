%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xtdml
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Double Machine Learning for Static Panel Models with Fixed Effects

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-mlr3 >= 0.5.0
BuildRequires:    R-CRAN-mlr3tuning >= 0.3.0
BuildRequires:    R-CRAN-mlr3learners >= 0.3.0
BuildRequires:    R-CRAN-mlr3misc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-readstata13 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-mlr3 >= 0.5.0
Requires:         R-CRAN-mlr3tuning >= 0.3.0
Requires:         R-CRAN-mlr3learners >= 0.3.0
Requires:         R-CRAN-mlr3misc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-readstata13 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-checkmate 

%description
Implementation of partially linear panel regression (PLPR) models with
high-dimensional confounding variables and exogenous treatment variable
within the double machine learning framework. It allows the estimation of
the structural parameter (treatment effect) in static panel data models
with fixed effects using panel data approaches established in Clarke and
Polselli (2025) <doi:10.1093/ectj/utaf011>. 'xtdml' is built on the
object-oriented 'DoubleML' (Bach et al., 2024) <doi:10.18637/jss.v108.i03>
using the 'mlr3' ecosystem.

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
