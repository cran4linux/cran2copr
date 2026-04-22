%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wdsmatch
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Double Score Matching for Survey-Weighted Causal Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements weighted double score matching (WDSM) for estimating
population-level causal effects from complex survey data. Combines
propensity scores and prognostic scores with survey design weights for
matching, survey-weighted imputation within match sets, and Hajek
normalization to target the population average treatment effect (PATE) and
the population average treatment effect on the treated (PATT). Supports
both retrospective (treatment-dependent) and prospective
(treatment-independent) sampling designs. Achieves double robustness:
consistent estimation when either the propensity score or prognostic score
model is correctly specified. Provides polynomial sieve bias correction
and linearization-based multinomial bootstrap variance estimation that
preserves the survey-weighted matching structure without re-matching.
Methods are described in Zeng, Tong, Tong, Lu, Mukherjee, and Li (2026,
under review) "Where to weight? Estimating population causal effects with
weighted double score matching in complex surveys".

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
