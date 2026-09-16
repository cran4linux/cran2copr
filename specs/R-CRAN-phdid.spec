%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phdid
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Homogeneity in Staggered Difference-in-Differences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
In staggered difference-in-differences designs the treatment effect is a
vector of cohort-time effects rather than a single number. Estimating each
separately is unbiased but imprecise when some are equal, while pooling
them all is precise but biased under genuine heterogeneity. This package
treats the choice as a partition-selection problem on the cohort-time
cells and provides two estimators for it: a Dirichlet process mixture
fitted by a collapsed Gibbs sampler, whose posterior marginalises over the
unknown partition and reports co-clustering probabilities, and an
'L0'-penalised estimator that returns a single partition and arises as the
fixed-variance maximum a posteriori solution of the same model. Also
provides tests for whether the cohort-time effects carry recoverable
heterogeneity at all, sampler diagnostics including exact enumeration of
the partition posterior for small designs, regularisation paths for both
estimators, and a calibrated data-generating process. All estimators
accept a vector of first-stage cohort-time effects with their joint
covariance, so any heterogeneity-robust first-stage estimator may be used.
Methods are described in Arora and Wagle (2026)
<doi:10.2139/ssrn.7207083>.

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
