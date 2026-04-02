%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SingleArmMRCT
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regional Consistency Probability for Single-Arm Multi-Regional Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-stats 

%description
Provides functions to calculate and visualise the Regional Consistency
Probability (RCP) for single-arm multi-regional clinical trials (MRCTs)
using the Effect Retention Approach (ERA). Six endpoint types are
supported: continuous, binary, count (negative binomial), time-to-event
via hazard ratio, milestone survival, and restricted mean survival time
(RMST). For each endpoint, both a closed-form (or semi-analytical)
solution and a Monte Carlo simulation approach are implemented. Two
consistency evaluation methods are available: Method 1 (effect retention
in Region 1 relative to the overall population) and Method 2 (simultaneous
positive effect across all regions). Plotting functions generate faceted
visualisations of RCP as a function of the regional allocation proportion,
overlaying formula and simulation results for direct comparison. The
methodology follows the Japanese MHLW guidelines for MRCTs. Abbreviations
used: RCP (Regional Consistency Probability), MRCT (Multi-Regional
Clinical Trial), RMST (Restricted Mean Survival Time), MHLW (Ministry of
Health, Labour and Welfare).

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
