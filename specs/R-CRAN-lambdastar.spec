%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lambdastar
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Measurement and Linear Hypothesis Models for Lambda Star

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-boot 

%description
Estimates intrinsic and captured noncentrality from parallel measurements
and evaluates the numerical parsimony functional for an explicitly encoded
hypothesis matrix, formula, or compatible linear model. Includes
common-case model comparisons, quantized entropy capacity, controlled
temperature integration, and explicit singularity diagnostics. Uses
manuscript projection estimates by default, with an explicit alternative
population estimator. Supports common nuisance adjustment and ordinary
case or cluster percentile bootstrap intervals, with diagnostics for
undefined estimates and preserved model coding. Provides reusable
row-bound design specifications and explicit conditional term blocks,
named linear restrictions, explicit predictor-grid contrasts, and fixed or
reevaluated basis recipes under a homogeneous isotropic
measurement-fluctuation assumption. Supports explicit known-reference mean
hypotheses and paired differences from parallel measurement pairs. Encodes
fixed person-by-occasion models with parallel indicators, implicit person
adjustment and whole-person bootstrap with distinct sampled copies. The
underlying method is described in Hammes (2026)
<doi:10.5281/zenodo.22962377>.

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
