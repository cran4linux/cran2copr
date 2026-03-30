%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drMAIC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Doubly Robust Matching-Adjusted Indirect Comparison for HTA

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggplot2 

%description
Implements Doubly Robust Matching-Adjusted Indirect Comparison (DR-MAIC)
for population-adjusted indirect treatment comparisons in health
technology appraisal (HTA). The package provides: (1) standard MAIC via
entropy balancing / exponential tilting; (2) augmented/doubly robust MAIC
combining inverse probability weighting with outcome regression; (3)
comprehensive covariate balance diagnostics including standardised mean
differences, Love plots, and effective sample size; (4) sensitivity
analyses including E-values, weight trimming, and variable exclusion
analyses; (5) bootstrap confidence intervals; and (6) submission-ready
outputs aligned with NICE Decision Support Unit Technical Support Document
18, Cochrane Handbook guidance on indirect comparisons, and ISPOR best
practice guidelines. Supports binary (risk difference, risk ratio, odds
ratio) and time-to-event (hazard ratio) outcomes.

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
