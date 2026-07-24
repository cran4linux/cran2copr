%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMCMC
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Contemporaneous Markov Chain Monte Carlo

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0

%description
Implements contemporaneous Markov chain Monte Carlo (CMCMC) and interchain
adaptive Markov chain Monte Carlo (INCA) samplers of Craiu, Rosenthal and
Yang (2009) <doi:10.1198/jasa.2009.tm08393> for targets known up to a
normalising constant. The samplers run multiple Metropolis chains in
parallel and update proposal covariance estimates using contemporaneous
particle groups. Built-in target kernels include multivariate normal,
logistic regression, Poisson, Gaussian, Gamma, and hierarchical models,
with support for user-provided target kernels. The formula interface
glm_cmcmc() fits supported generalized linear models using the built-in
kernels. 'CUDA' is used when available, and an 'OpenMP'-enabled CPU
backend is available on systems without a 'CUDA' compiler.

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
