%global __brp_check_rpaths %{nil}
%global packname  crossvalidationCP
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validation for Change-Point Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-changepoint >= 2.0
BuildRequires:    R-CRAN-stepR >= 2.0
BuildRequires:    R-CRAN-wbs >= 1.4
BuildRequires:    R-CRAN-FDRSeg >= 1.0.3
BuildRequires:    R-stats 
Requires:         R-CRAN-changepoint >= 2.0
Requires:         R-CRAN-stepR >= 2.0
Requires:         R-CRAN-wbs >= 1.4
Requires:         R-CRAN-FDRSeg >= 1.0.3
Requires:         R-stats 

%description
Implements the cross-validation methodology from Pein and Shah (2021)
<arXiv:2112.03220>. Can be customised by providing different
cross-validation criteria, estimators for the change-point locations and
local parameters, and freely chosen folds. Pre-implemented estimators and
criteria are available. It also includes our own implementation of the
COPPS procedure <doi:10.1214/19-AOS1814>.

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
