%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TieFreeCensor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithm for Generating Tie-Free Progressive Type-II Censored Samples

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Generates tie-free progressive Type-II censored samples from discrete
distributions and user-specified discrete probability mass functions (PMF)
or cumulative distribution functions (CDF). Provides maximum likelihood
estimation (MLE), Bayesian estimation via Markov chain Monte Carlo (MCMC)
Metropolis-within-Gibbs sampling, likelihood-based parametric bootstrap
goodness-of-fit (GOF) tests, profile log-likelihood diagnostics, and
discrete survival and probability calculations. Methods are based on Ahmad
and Mansour (2026) <doi:10.1155/jom/3657078>, Balakrishnan and Dembinska
(2008) <doi:10.1016/j.jspi.2007.02.006>, Joe and Zhu (2005)
<doi:10.1002/bimj.200410102>, and Balakrishnan and Aggarwala (2000,
ISBN:978-1-4612-1334-5).

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
