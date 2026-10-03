%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mudnester
%global packver   0.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.8
Release:          1%{?dist}%{?buildtag}
Summary:          Surveillance Data Cleaning and Preparation for Public Health

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-janitor >= 2.2.0
BuildRequires:    R-CRAN-lubridate >= 1.9.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-digest >= 0.6.30
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-janitor >= 2.2.0
Requires:         R-CRAN-lubridate >= 1.9.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-digest >= 0.6.30
Requires:         R-utils 
Requires:         R-stats 

%description
Clean, prepare, and aggregate surveillance data for public health
analysis. Provides structural data cleaning and standardisation
(clean_the_nest()), age categorisation against ~50 published schemes with
publication-ready labelling (preening()), time-unit aggregation with
zero-filling and seasonal awareness (roost()), joint aggregation of
several linked event dates (e.g. onset, admission, ICU, complication,
fatality) into one table of comparable rate columns (flyway()),
under-ascertainment correction via a stratified, time-varying multiplier
factor supplied directly, derived by the ratio (multiplier) method, or
derived by inverting an externally sourced severity rate (e.g. an
infection-fatality-rate anchor) against an observed severity ratio
(corncrake()), comorbidity detection from ICD-10-AM clinical coding
(plumage()), vaccine coverage data construction (brood()), hash-based
de-identification (molting()), and relinking of previously de-identified
data (homing()). brood() produces a brood_df object supporting two
population models: pre-aggregated denominators (population_model =
"pre_aggregated") and record-level cohort designs (population_model =
"cohort"). The cohort model handles single time-point coverage snapshots,
interrupted time series analysis via a built-in sweep returning monthly
coverage rates (time_series = TRUE), and birth cohort designs with
person-time computation. This cohort/time-series coverage model was
applied in Roughan et al. (2026) <doi:10.33321/cdi.2026.50.031> to
estimate infant immunisation coverage against respiratory syncytial virus
over an 18-month period. Both wide format (one row per person with dose
columns, from 'starling'::murmuration()) and long format (one row per
dose) are accepted. corncrake() returns both a point-corrected count and
uncertainty bounds wherever they can be derived, including the inverse
relationship between a severity-anchored factor and the bounds of its own
reference rate. Built for Australian public health surveillance practice
but not specific to it -- see individual function documentation for notes
on non-Australian use (e.g. Northern Hemisphere season boundaries).

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
