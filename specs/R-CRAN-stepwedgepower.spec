%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stepwedgepower
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Stepped-Wedge Clinical Trial Analysis and Power Simulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-lme4 

%description
Provides reusable functions for aggregated cluster-period data,
mixed-effects analysis, and simulation-based power and type I error
evaluation in stepped-wedge cluster randomized trials. The design and
mixed-effects analysis follow Hussey and Hughes (2007)
<doi:10.1016/j.cct.2006.05.007>. Intraclass correlations for binary
outcomes are converted to logistic-normal random-intercept standard
deviations following Eldridge, Ukoumunne and Carlin (2009)
<doi:10.1111/j.1751-5823.2009.00092.x>. Monte Carlo uncertainty in
estimated power is summarized using the exact binomial interval of Clopper
and Pearson (1934) <doi:10.1093/biomet/26.4.404>. The simulation engine
supports sequence-specific baseline risks, cluster random effects, direct
intraclass-correlation specification, Monte Carlo uncertainty intervals,
and model-fitting diagnostics. Applied physician and specialty helpers are
retained for backward compatibility and for an example health-services
workflow.

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
