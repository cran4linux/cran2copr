%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggdmcLikelihood
%global packver   0.2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood Computation for 'ggdmc' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.7.5.0
BuildRequires:    R-CRAN-ggdmcHeaders 
Requires:         R-CRAN-Rcpp >= 1.0.7

%description
Efficient computation of likelihoods in design-based choice response time
models, including the Decision Diffusion Model, is supported. The package
enables rapid evaluation of likelihood functions for both single- and
multi-subject models across trial-level data. It also offers fast
initialisation of starting parameters for genetic sampling with many
Markov chains, facilitating estimation in complex models typically found
in experimental psychology and behavioural science. These optimisations
help reduce computational overhead in large-scale model fitting tasks.

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
