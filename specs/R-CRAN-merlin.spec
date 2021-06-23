%global __brp_check_rpaths %{nil}
%global packname  merlin
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Mixed Effects Regression for Linear, Non-Linear and User-DefinedModels

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-tools 
Requires:         R-MASS 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-tools 

%description
Fits linear, non-linear, and user-defined mixed effects regression models
following the framework developed by Crowther (2017) <arXiv:1710.02223>.
'merlin' can fit multivariate outcome models of any type, each of which
could be repeatedly measured (longitudinal), with any number of levels,
and with any number of random effects at each level. Standard
distributions/models available include the Bernoulli, Gaussian, Poisson,
beta, negative-binomial, and time-to-event/survival models include the
exponential, Gompertz, Royston-Parmar, Weibull and general hazard model.
'merlin' provides a flexible predictor syntax, allowing the user to define
variables, random effects, spline and fractional polynomial functions,
functions of other outcome models, and any interaction between each of
them. Non-linear and time-dependent effects are seamlessly incorporated
into the predictor. 'merlin' allows multivariate normal random effects,
which are integrated out using Gaussian quadrature or Monte-Carlo
integration. Note, 'merlin' is based on the 'Stata' package of the same
name, described in Crowther (2018) <arXiv:1806.01615>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
