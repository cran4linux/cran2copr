%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesAiken
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Content Validity Coefficients with Credibility Intervals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Bayesian inference for the six rating coefficients proposed by Aiken
(1985) <doi:10.1177/0013164485451012> and Aiken (1989)
<doi:10.1177/0013164489492003>: V (content validity), H (homogeneity), C
(congruence), R (repeatability), A (rater agreement) and I (item
coherence). All six are expressed as functionals of the population
distribution of rating categories, so a single Dirichlet-Multinomial model
yields their full posterior by push-forward. This treats each judge as one
categorical observation and avoids the pseudo-replication of Beta-Binomial
formulations. R is modelled on the c-by-c joint table because it is not a
functional of the marginal distribution. Provides classical estimates with
the correct parity correction, highest density and equal-tailed
credibility intervals, posterior threshold probabilities, prior
sensitivity analysis and a friendly step-by-step verbose report.

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
