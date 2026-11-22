%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MFF
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Meta Fuzzy Functions for Aggregating Prediction Pools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-parallel 
Requires:         R-CRAN-e1071 
Requires:         R-parallel 

%description
Aggregates numeric candidate predictions using Meta Fuzzy Functions and
membership-derived weights learned on validation predictions, following
Tak (2018) <doi:10.1016/j.asoc.2018.08.009> and Tak (2021)
<doi:10.1016/j.ins.2021.01.024>. Provides a common prediction-pool
interface, fixed and tuned fits, explicit validation-based selection, and
standard methods for inspecting weights, predicting and plotting results.
Candidate pools may contain different regression learners, bootstrap fits,
alternative hyperparameter configurations, or externally generated
regression and time-aligned forecasting predictions. Resampling results of
'caret' and 'tidymodels' can be converted into pools, and forecasting
pools are built by rolling-origin evaluation or from 'fable' forecasts.
Supports fuzzy c-means, possibilistic fuzzy c-means following Pal et al.
(2005) <doi:10.1109/TFUZZ.2004.840099>, Gustafson-Kessel clustering with
the improved covariance estimation of Babuska et al. (2002)
<doi:10.1109/FUZZ.2002.1006654> and k-means clustering. Optional helpers
train built-in or user-defined regression learners on explicit data
splits, cross-validation folds or bootstrap samples.

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
