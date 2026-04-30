%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BivLaplaceRL
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Laplace Transforms, Stochastic Orders, and Entropy Measures in Reliability

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements methods for bivariate Laplace transforms of residual lives and
reversed residual lives, associated stochastic ordering concepts, and
dynamic entropy measures for reliability analysis. The package covers
three primary research areas: (1) Bivariate Laplace transform of residual
lives and stochastic comparisons based on the bivariate Laplace transform
order of residual lives (BLt-rl), including weak bivariate hazard rate,
mean residual life, and relative mean residual life orders, nonparametric
estimation, and NBUHR/NWUHR aging class characterisation (Jayalekshmi,
Rajesh, and Nair, 2022, <doi:10.1080/03610926.2022.2085874>); (2)
Bivariate Laplace transform order of reversed residual lives (BLt-Rrl),
reversed hazard gradient, reversed mean residual life, and the associated
stochastic orders (weak bivariate reversed hazard rate, weak bivariate
reversed mean residual life); (3) Residual entropy generating function, a
dynamic version of Golomb's (1966) information generating function whose
derivative yields the residual entropy of Ebrahimi and Pellerey (1995),
with nonparametric estimation and distribution characterisation.
Parametric families supported include the Gumbel bivariate exponential,
Farlie-Gumbel-Morgenstern (FGM), bivariate power, and Schur-constant
distributions.  Plotting utilities and a simulation framework for
evaluating estimator performance are also provided.

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
