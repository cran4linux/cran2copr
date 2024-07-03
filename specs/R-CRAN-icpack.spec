%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icpack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Analysis of Interval-Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-survival >= 3.1
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 

%description
Survival analysis of interval-censored data with proportional hazards, and
an explicit smooth estimate of the baseline log-hazard with P-splines.

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
