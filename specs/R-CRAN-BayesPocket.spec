%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesPocket
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Causal Inference for Periodontal Diseases in Longitudinal Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats >= 4.4.2
BuildRequires:    R-parallel >= 4.4.2
BuildRequires:    R-CRAN-pbmcapply >= 1.5.1
BuildRequires:    R-CRAN-progress >= 1.2.3
BuildRequires:    R-CRAN-truncnorm >= 1.0.9
BuildRequires:    R-CRAN-SoftBart >= 1.0.3
BuildRequires:    R-CRAN-GIGrvg >= 0.8
BuildRequires:    R-CRAN-stochtree >= 0.1.1
Requires:         R-stats >= 4.4.2
Requires:         R-parallel >= 4.4.2
Requires:         R-CRAN-pbmcapply >= 1.5.1
Requires:         R-CRAN-progress >= 1.2.3
Requires:         R-CRAN-truncnorm >= 1.0.9
Requires:         R-CRAN-SoftBart >= 1.0.3
Requires:         R-CRAN-GIGrvg >= 0.8
Requires:         R-CRAN-stochtree >= 0.1.1

%description
Implements the Mixed Treatment-State Causal Model (MTSCM), a Bayesian
framework for estimating causal effects of clinical interventions on
bounded continuous outcomes in longitudinal observational studies with
irregular visits. The methodology is specifically designed for periodontal
disease research, where discrete treatments and continuous disease states
(e.g., proportion of periodontal pockets exceeding 3 mm) reciprocally
influence one another under dynamic feedback. The package integrates a
double-censored Tobit likelihood to handle boundary mass at zero and one,
subject-specific random effects to capture within-subject correlation, and
flexible tree-based ensemble priors (standard BART and Soft BART) to model
complex nonlinear interactions without parametric restrictions. Causal
identification is established under the potential outcomes framework via
the G-computation formula, with key estimands including the Mixed Average
Potential Outcome (MAPO) and the Mixed Probability of Disease Resolution
(MPDR). The package provides functions for model fitting, posterior
inference, and causal estimand estimation.

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
