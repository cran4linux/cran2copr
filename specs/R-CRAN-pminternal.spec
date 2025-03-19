%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pminternal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Internal Validation of Clinical Prediction Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dcurves 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-marginaleffects 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pmcalibration 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-dcurves 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-marginaleffects 
Requires:         R-methods 
Requires:         R-CRAN-pmcalibration 
Requires:         R-CRAN-pROC 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-purrr 

%description
Conduct internal validation of a clinical prediction model for a binary
outcome. Produce bias corrected performance metrics (c-statistic, Brier
score, calibration intercept/slope) via bootstrap (simple bootstrap,
bootstrap optimism, .632 optimism) and cross-validation (CV optimism, CV
average). Also includes functions to assess model stability via bootstrap
resampling. See Steyerberg et al. (2001)
<doi:10.1016/s0895-4356(01)00341-9>; Harrell (2015)
<doi:10.1007/978-3-319-19425-7>; Riley and Collins (2023)
<doi:10.1002/bimj.202200302>.

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
