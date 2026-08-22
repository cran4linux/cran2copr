%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoxAalenCR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Additive-Multiplicative Cox-Aalen Subdistribution Hazard Model for Competing Risks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-survival 

%description
Implements the flexible additive-multiplicative Cox-Aalen subdistribution
hazard regression model for competing risks data as proposed by Li and
Long (2019) <doi:10.1007/s11424-019-7281-6>. The framework accommodates
both time-varying non-parametric additive covariate effects through an
Aalen (1980) additive model and constant multiplicative effects via a Cox
proportional hazards structure, generalizing Scheike and Zhang (2002)
<doi:10.1111/1467-9469.00065> and Martinussen and Scheike (2002)
<doi:10.1093/biomet/89.2.283>. Includes inverse probability of censoring
weighting (IPCW) with both Kaplan-Meier weights (Fine and Gray, 1999
<doi:10.1080/01621459.1999.10474144>) and covariate-dependent Cox
censoring weights (He et al., 2016 <doi:10.1111/sjos.12172>; Li and Long,
2019 <doi:10.1007/s11424-019-7281-6>). Provides simultaneous estimating
equations based on Huffer and McKeague (1991)
<doi:10.1080/01621459.1991.10475010>, asymptotic sandwich variance
estimation with censoring-weight martingale corrections, cumulative
incidence function (CIF) prediction with pointwise confidence intervals,
supremum-type goodness-of-fit tests for time-varying covariate effects,
and Monte Carlo competing risks data simulation.

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
