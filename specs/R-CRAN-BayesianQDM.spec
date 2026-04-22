%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianQDM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Quantitative Decision-Making Framework for Binary and Continuous Endpoints

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Provides comprehensive methods to calculate posterior probabilities,
posterior predictive probabilities, and Go/NoGo/Gray decision
probabilities for quantitative decision-making under a Bayesian paradigm
in clinical trials. The package supports both single and two-endpoint
analyses for binary and continuous outcomes, with controlled,
uncontrolled, and external designs. For single continuous endpoints, three
calculation methods are available: numerical integration (NI), Monte Carlo
simulation (MC), and Moment-Matching approximation (MM). For two
continuous endpoints, a bivariate Normal-Inverse-Wishart conjugate model
is implemented with MC and MM methods. For two binary endpoints, a
Dirichlet-multinomial model is implemented. External designs incorporate
historical data through power priors using exact conjugate representations
(Normal-Inverse-Chi-squared for single continuous, Normal-Inverse-Wishart
for two continuous, and Dirichlet for binary endpoints), enabling
closed-form posterior computation without Markov chain Monte Carlo (MCMC)
sampling. This approach significantly reduces computational burden while
preserving complete Bayesian rigor. The package also provides grid-search
functions to find optimal Go and NoGo thresholds that satisfy
user-specified operating characteristic criteria for all supported
endpoint types and study designs. S3 print() and plot() methods are
provided for all decision probability classes, enabling formatted display
and visualisation of Go/NoGo/Gray operating characteristics across
treatment scenarios. See Kang, Yamaguchi, and Han (2026)
<doi:10.1080/10543406.2026.2655410> for the methodological framework.

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
