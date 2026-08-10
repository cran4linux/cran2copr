%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MiCT
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Minimal Important Change and Threshold Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-pROC 

%description
Provides methods for estimating minimal important change (MIC) and
interpretation thresholds for multi-item questionnaires and single-item
continuous or ordinal measures. Methods include predictive modelling,
adjusted predictive modelling, improved adjusted predictive modelling
using anchor reliability, confirmatory factor analysis for anchor
reliability, longitudinal confirmatory factor analysis for MIC estimation,
longitudinal confirmatory factor analysis-based MIC estimation for
single-item measures, and confirmatory factor analysis-based threshold
estimation for single-item and multi-item measures. Implemented methods
include those developed by Terluin et al. (2015)
<doi:10.1016/j.jclinepi.2015.03.015>, Terluin et al. (2017)
<doi:10.1016/j.jclinepi.2016.12.015>, Terluin et al. (2022)
<doi:10.1016/j.jclinepi.2022.04.018>, Terluin et al. (2023)
<doi:10.1007/s11136-023-03355-8>, Terluin et al. (2024)
<doi:10.1007/s11136-023-03577-w>, Terluin et al. (2024)
<doi:10.1007/s11136-024-03763-4>, and Terluin et al. (2026)
<doi:10.1007/s11136-025-04134-3>.

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
