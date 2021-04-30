%global packname  daySupply
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Days' Supply and Daily Dose of Prescriptions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
Allows clinicians and researchers to compute daily dose (and subsequently
days' supply) for prescription refills using the following methods: Fixed
window, fixed tablet, defined daily dose (DDD), and Random Effects
Warfarin Days' Supply (REWarDS). Daily dose is the computed dose that the
patient takes every day. For medications with fixed dosing (e.g. direct
oral anticoagulants) this is known and does not need to be estimated. For
medications with varying dose such as warfarin, however, the daily dose
should be assumed or estimated to allow measurement of drug exposure.
Days’ supply is the number of days that patients’ supply of medication
will last after each prescription fill. Estimating days’ supply is
necessary to calculate drug exposure. The package computes days’ supply
and daily dose at both the prescription and patient levels. Results at the
prescription level are denoted with “-Rx-” and those at patient level are
denoted with “-Pt-”.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
