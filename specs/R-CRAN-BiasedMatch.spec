%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BiasedMatch
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Biased Matching for Two-Urn Sampling Problems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for the two-urn biased sampling problems of Puza and Bonfrer (2018)
<doi:10.1080/03610926.2017.1300282>. Two overlapping sets of items are
sampled without replacement, with items common to both sets given a
selection weight favouring their inclusion. The package computes the
probability mass function, mean and variance of the number of matching
items using the univariate and bivariate Wallenius' non-central
hypergeometric distributions, performs maximum likelihood and Bayesian
inference for the bias parameter, and provides Metropolis-Hastings
algorithms for hierarchical extensions.

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
