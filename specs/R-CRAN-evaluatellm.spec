%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evaluatellm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference for Language Model Evaluations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Treats language model evaluations as statistical experiments and supplies
the inference they require. Provides central limit theorem and
cluster-robust standard errors for evaluation scores, paired and unpaired
model comparisons, variance decomposition when several responses are drawn
per question, control-variate variance reduction, multiplicity adjustment
across benchmark suites, and power and minimum detectable effect
calculations for planning evaluations, following Miller (2024)
<doi:10.48550/arXiv.2411.00640>. For evaluations scored by a model judge,
implements agreement statistics against a human gold standard and
prediction-powered inference (Angelopoulos et al. 2023)
<doi:10.1126/science.adi6000> with the power-tuned estimator of
Angelopoulos, Bates and Jordan (2023) <doi:10.48550/arXiv.2311.01453>, so
a small set of human labels debiases a large set of judge scores.
Leaderboards are supported through bootstrap rank intervals and
Bradley-Terry ratings (Bradley and Terry 1952) <doi:10.2307/2334029>.
Accepts scores from any evaluation harness.

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
