%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qspquest
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pharmacology Model Simulation and Bounded Estimation

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-jsonlite >= 2.0.0
Requires:         R-CRAN-jsonlite >= 2.0.0

%description
Compile pharmacokinetic, pharmacodynamic and quantitative systems
pharmacology models with explicit physical units, then simulate dosing
regimens, run parameter scans and Morris (1991)
<doi:10.1080/00401706.1991.10484804> elementary-effects screens.
Parameters are estimated within declared bounds by maximum likelihood or
maximum a posteriori fitting for individual and pooled data, and by
first-order conditional estimation with interaction (Wang 2007
<doi:10.1007/s10928-007-9060-6>) or stochastic approximation
expectation-maximization (Kuhn and Lavielle 2005
<doi:10.1016/j.csda.2004.07.002>) for population data. Count and
correlated binomial data can be fitted with Gamma-Poisson and
probit-normal mixture models. A documented subset of 'NONMEM'-style dosing
and observation records can be converted to model requests with source-row
provenance. Computation uses the 'QSPQuest' engine, written in 'Rust',
with stiff ordinary differential equation solvers from the 'diffsol'
library.

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
