%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TTM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Terminal Trend Models on the Retrospective Time Scale

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-geer 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-geer 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-magrittr 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 

%description
Fits retrospective-time longitudinal models for terminal trend analysis
using weighted generalized estimating equations and related joint modeling
tools. The package provides functions to estimate spline-based baseline
and treatment effect trajectories on the retrospective time scale, obtain
pointwise confidence intervals, and visualize fitted trajectories.

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
