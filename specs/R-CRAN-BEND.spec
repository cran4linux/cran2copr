%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BEND
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of Nonlinear Data (BEND)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.3
Requires:         R-core >= 3.6.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.14
BuildRequires:    R-CRAN-label.switching >= 1.8
BuildRequires:    R-CRAN-coda >= 0.19.4
Requires:         R-CRAN-rjags >= 4.14
Requires:         R-CRAN-label.switching >= 1.8
Requires:         R-CRAN-coda >= 0.19.4

%description
Provides a set of models to estimate nonlinear longitudinal data using
Bayesian estimation methods. These models include the: 1) Bayesian
Piecewise Random Effects Model (Bayes_PREM()) which estimates a piecewise
random effects (mixture) model for a given number of latent classes and a
latent number of possible changepoints in each class, and can incorporate
class and outcome predictive covariates (see Lamm (2022)
<https://hdl.handle.net/11299/252533> and Lock et al., (2018)
<doi:10.1007/s11336-017-9594-5>), 2) Bayesian Crossed Random Effects Model
(Bayes_CREM()) which estimates a linear, quadratic, exponential, or
piecewise crossed random effects models where individuals are changing
groups over time (e.g., students and schools; see Rohloff et al., (2024)
<doi:10.1111/bmsp.12334>), and 3) Bayesian Bivariate Piecewise Random
Effects Model (Bayes_BPREM()) which estimates a bivariate piecewise random
effects model to jointly model two related outcomes (e.g., reading and
math achievement; see Peralta et al., (2022) <doi:10.1037/met0000358>).

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
