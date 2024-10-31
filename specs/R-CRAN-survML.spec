%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survML
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Flexible Survival Analysis Using Machine Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 4.3.2
BuildRequires:    R-methods >= 4.3.2
BuildRequires:    R-CRAN-gtools >= 3.9.5
BuildRequires:    R-CRAN-survival >= 3.5.0
BuildRequires:    R-CRAN-mboost >= 2.9.0
BuildRequires:    R-CRAN-SuperLearner >= 2.0.28
BuildRequires:    R-CRAN-fdrtool >= 1.2.17
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-haldensify >= 0.2.3
BuildRequires:    R-CRAN-ChernoffDist >= 0.1.0
BuildRequires:    R-CRAN-Iso >= 0.0.18.1
Requires:         R-stats >= 4.3.2
Requires:         R-methods >= 4.3.2
Requires:         R-CRAN-gtools >= 3.9.5
Requires:         R-CRAN-survival >= 3.5.0
Requires:         R-CRAN-mboost >= 2.9.0
Requires:         R-CRAN-SuperLearner >= 2.0.28
Requires:         R-CRAN-fdrtool >= 1.2.17
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-haldensify >= 0.2.3
Requires:         R-CRAN-ChernoffDist >= 0.1.0
Requires:         R-CRAN-Iso >= 0.0.18.1

%description
Statistical tools for analyzing time-to-event data using machine learning.
Implements survival stacking for conditional survival estimation,
standardized survival function estimation for current status data, and
methods for algorithm-agnostic variable importance. See Wolock CJ, Gilbert
PB, Simon N, and Carone M (2024) <doi:10.1080/10618600.2024.2304070>.

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
