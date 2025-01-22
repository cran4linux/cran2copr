%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survPen
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Penalized Splines for (Excess) Hazard Models, Relative Mortality Ratio Models and Marginal Intensity Models

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-statmod 
Requires:         R-stats 

%description
Fits (excess) hazard, relative mortality ratio or marginal intensity
models with multidimensional penalized splines allowing for time-dependent
effects, non-linear effects and interactions between several continuous
covariates. In survival and net survival analysis, in addition to
modelling the effect of time (via the baseline hazard), one has often to
deal with several continuous covariates and model their functional forms,
their time-dependent effects, and their interactions. Model specification
becomes therefore a complex problem and penalized regression splines
represent an appealing solution to that problem as splines offer the
required flexibility while penalization limits overfitting issues. Current
implementations of penalized survival models can be slow or unstable and
sometimes lack some key features like taking into account expected
mortality to provide net survival and excess hazard estimates. In
contrast, survPen provides an automated, fast, and stable implementation
(thanks to explicit calculation of the derivatives of the likelihood) and
offers a unified framework for multidimensional penalized hazard and
excess hazard models. Later versions (>2.0.0) include penalized models for
relative mortality ratio, and marginal intensity in recurrent event
setting. survPen may be of interest to those who 1) analyse any kind of
time-to-event data: mortality, disease relapse, machinery breakdown,
unemployment, etc 2) wish to describe the associated hazard and to
understand which predictors impact its dynamics, 3) wish to model the
relative mortality ratio between a cohort and a reference population, 4)
wish to describe the marginal intensity for recurrent event data. See
Fauvernier et al. (2019a) <doi:10.21105/joss.01434> for an overview of the
package and Fauvernier et al. (2019b) <doi:10.1111/rssc.12368> for the
method.

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
