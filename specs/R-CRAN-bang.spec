%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bang
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis, No Gibbs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rust >= 1.2.2
BuildRequires:    R-CRAN-bayesplot >= 1.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-rust >= 1.2.2
Requires:         R-CRAN-bayesplot >= 1.1.0
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides functions for the Bayesian analysis of some simple commonly-used
models, without using Markov Chain Monte Carlo (MCMC) methods such as
Gibbs sampling.  The 'rust' package
<https://cran.r-project.org/package=rust> is used to simulate a random
sample from the required posterior distribution, using the generalized
ratio-of-uniforms method.  See Wakefield, Gelfand and Smith (1991)
<DOI:10.1007/BF01889987> for details. At the moment three conjugate
hierarchical models are available: beta-binomial, gamma-Poisson and a
1-way analysis of variance (ANOVA).

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
