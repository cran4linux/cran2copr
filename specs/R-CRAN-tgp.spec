%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tgp
%global packver   2.4-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.19
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Treed Gaussian Process Models

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-maptree 
Requires:         R-CRAN-maptree 

%description
Bayesian nonstationary, semiparametric nonlinear regression and design by
treed Gaussian processes (GPs) with jumps to the limiting linear model
(LLM).  Special cases also implemented include Bayesian linear models,
CART, treed linear models, stationary separable and isotropic GPs, and GP
single-index models.  Provides 1-d and 2-d plotting functions (with
projection and slice capabilities) and tree drawing, designed for
visualization of tgp-class output.  Sensitivity analysis and
multi-resolution models are supported. Sequential experimental design and
adaptive sampling functions are also provided, including ALM, ALC, and
expected improvement.  The latter supports derivative-free optimization of
noisy black-box functions.  For details and tutorials, see Gramacy (2007)
<doi:10.18637/jss.v019.i09> and Gramacy & Taddy (2010)
<doi:10.18637/jss.v033.i06>.

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
