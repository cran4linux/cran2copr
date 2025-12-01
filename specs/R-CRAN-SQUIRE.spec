%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SQUIRE
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Quality-Assured Integrated Response Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GALAHAD >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-GALAHAD >= 1.0.0
Requires:         R-stats 
Requires:         R-CRAN-knitr 

%description
Provides systematic geometry-adaptive parameter optimization with
statistical validation for experimental biological data. Combines
ANOVA-based validation with systematic constraint configuration testing
(log-scale, positive domain, Euclidean) through T,P,E testing. Only
proceeds with parameter optimization when statistically significant
biological effects are detected, preventing over-fitting to noise. Uses
'GALAHAD' trust region methods with constraint projection from Conn et al.
(2000) <doi:10.1137/S1052623497325107>, ANOVA-based validation following
Fisher (1925) <doi:10.1007/978-1-4612-4380-9_6>, and effect size
calculations per Cohen (1988, ISBN:0805802835). Designed for structured
experimental data including kinetic curves, dose-response studies, and
treatment comparisons where appropriate parameter constraints and
statistical justification are important for meaningful biological
interpretation. Developed at the Minnesota Center for Prion Research and
Outreach at the University of Minnesota.

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
