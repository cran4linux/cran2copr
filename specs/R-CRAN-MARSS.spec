%global __brp_check_rpaths %{nil}
%global packname  MARSS
%global packver   3.11.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.11.4
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Autoregressive State-Space Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-KFAS >= 1.0.1
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-KFAS >= 1.0.1
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-utils 

%description
The MARSS package provides maximum-likelihood parameter estimation for
constrained and unconstrained linear multivariate autoregressive
state-space (MARSS) models fit to multivariate time-series data.  Fitting
is primarily via an Expectation-Maximization (EM) algorithm, although
fitting via the BFGS algorithm (using the optim function) is also
provided.  MARSS models are a class of dynamic linear model (DLM) and
vector autoregressive model (VAR) model.  Functions are provided for
parametric and innovations bootstrapping, Kalman filtering and smoothing,
bootstrap model selection criteria (AICb), confidences intervals via the
Hessian approximation and via bootstrapping and calculation of auxiliary
residuals for detecting outliers and shocks.  The user guide shows
examples of using MARSS for parameter estimation for a variety of
applications, model selection, dynamic factor analysis, outlier and shock
detection, and addition of covariates.  Online workshops (lectures, eBook,
and computer labs) at <https://atsa-es.github.io/> See the NEWS file for
update information.

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
