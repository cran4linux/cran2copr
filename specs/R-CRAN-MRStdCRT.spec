%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRStdCRT
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Robust Standardization in Cluster-Randomized Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme >= 3.1.150
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-geepack >= 1.3.2
BuildRequires:    R-CRAN-lme4 >= 1.1.25
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-stats 
Requires:         R-CRAN-nlme >= 3.1.150
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-geepack >= 1.3.2
Requires:         R-CRAN-lme4 >= 1.1.25
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-stats 

%description
Implements model-robust standardization for cluster-randomized trials
(CRTs). Provides functions that standardize user-specified regression
models to estimate marginal treatment effects. The targets include the
cluster-average and individual-average treatment effects, with utilities
for variance estimation and example simulation datasets. Methods are
described in Li, Tong, Fang, Cheng, Kahan, and Wang (2025)
<doi:10.1002/sim.70270>.

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
