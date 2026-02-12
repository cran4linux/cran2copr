%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  likelihood.model
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood-Based Statistical Inference in the Fisherian Tradition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-algebraic.mle 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-algebraic.mle 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-generics 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-R6 

%description
Facilitates building likelihood models in the Fisherian tradition
following Richard Royall (1997, ISBN:978-0412044113) "Statistical
Evidence: A Likelihood Paradigm". Defines generic methods for working with
likelihoods (loglik(), score(), hess_loglik(), fim()) and provides
functions for pure likelihood-based inference (support(),
relative_likelihood(), likelihood_interval(), profile_loglik()). Includes
a likelihood contributions model for heterogeneous observation types
(exact, censored, etc.) assuming i.i.d. data.

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
