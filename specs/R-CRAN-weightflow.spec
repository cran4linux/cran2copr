%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weightflow
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Declarative Recipes for Staged Survey Weighting with Recipe-Aware Replicate Variances

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
an ordered recipe of explicit adjustments, estimated in a single call.
Steps cover within-cluster selection, subsampling for two-phase designs,
nonresponse by weighting classes or response-propensity models (optionally
machine-learning, with cross-fitting), calibration to known totals
following Deville and Sarndal (1992) <doi:10.2307/2290268>, optionally
model-assisted, non-probability samples by pseudo-weighting, mass
imputation and doubly robust estimators, and range-restricted trimming.
Rotating and pure panels add panel-selection probabilities, attrition,
longitudinal weights, gross flows and composite estimation. Variances come
from a recipe-aware bootstrap and jackknife that resample or delete
primary sampling units and re-apply the entire cascade on each replicate,
following Rao and Wu (1988) <doi:10.1080/01621459.1988.10478591>; panel
replicates are coordinated across waves, so the sample overlap enters the
variance of a net change as covariance, and two-phase variances split into
first- and second-phase components (V = V1 + V2). A self-contained HTML
report documents each step, and the weights bridge to the 'survey' and
'srvyr' packages. The methods, and the simulation evidence behind the
variance estimators, are described in Ferreira (2026)
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
