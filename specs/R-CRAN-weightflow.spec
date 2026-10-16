%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weightflow
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weighting Probability and Non-Probability Survey Samples with Recipe-Aware Replicate Variances

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-parallel 

%description
Builds survey analysis weights by declaring the whole weighting process as
an ordered recipe of explicit adjustments, estimated in a single call:
unknown eligibility, within-cluster selection, two-phase subsampling,
nonresponse by weighting classes or response-propensity models,
calibration and trimming. Calibration to known totals runs on linear,
raking or logit distances, bounded, ridge-penalized, model-assisted or
integrative with one weight per cluster; a calibrated trim bounds the
weights while keeping the control totals exact. Non-probability samples
are weighted against a probability reference sample by pseudo-weighting,
mass imputation and doubly robust estimators that calibrate a single
weight on the fitted values of several working models and on the
population totals of the auxiliaries at once, so one multipurpose weight
serves many variables. Variances come from a recipe-aware bootstrap and
jackknife that re-apply the entire cascade on each replicate, so every
adjustment is inside the variance instead of being treated as fixed;
across panel waves the replicates are coordinated by carrying forward the
selection multiplicities of the sampling units, so the sample overlap
enters the variance of a net change as covariance. Rotating and pure
panels add attrition, longitudinal weights, gross flows and composite
estimation, a self-contained HTML report documents each step, and the
weights bridge to the 'survey' and 'srvyr' packages, which are optional:
the package itself runs on base R. The methods, and the simulation
evidence behind the variance estimators, are described in Ferreira (2026)
<doi:10.1177/18747655261484262>.

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
