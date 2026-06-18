%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SelfControlledCohort
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Self-Controlled Cohort Population-Level Estimation

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector >= 5.0.0
BuildRequires:    R-CRAN-SqlRender >= 1.4.3
BuildRequires:    R-CRAN-ParallelLogger 
BuildRequires:    R-CRAN-rateratio.test 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EmpiricalCalibration 
BuildRequires:    R-CRAN-ResultModelManager 
BuildRequires:    R-CRAN-Andromeda 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
Requires:         R-CRAN-DatabaseConnector >= 5.0.0
Requires:         R-CRAN-SqlRender >= 1.4.3
Requires:         R-CRAN-ParallelLogger 
Requires:         R-CRAN-rateratio.test 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EmpiricalCalibration 
Requires:         R-CRAN-ResultModelManager 
Requires:         R-CRAN-Andromeda 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-stats 

%description
Estimates incidence rate ratios by comparing time exposed with time
unexposed among an exposed cohort using self-controlled cohort methodology
as described in Ryan et al. (2013) <doi:10.1002/pds.3457>. Functions used
for empirical calibration of effect estimates, confidence intervals, and
p-values are included to control for residual bias.

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
