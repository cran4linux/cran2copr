%global packname  jagsUI
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Wrapper Around 'rjags' to Streamline 'JAGS' Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 3.13
BuildRequires:    R-CRAN-coda >= 0.13
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-rjags >= 3.13
Requires:         R-CRAN-coda >= 0.13
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
A set of wrappers around 'rjags' functions to run Bayesian analyses in
'JAGS' (specifically, via 'libjags').  A single function call can control
adaptive, burn-in, and sampling MCMC phases, with MCMC chains run in
sequence or in parallel. Posterior distributions are automatically
summarized (with the ability to exclude some monitored nodes if desired)
and functions are available to generate figures based on the posteriors
(e.g., predictive check plots, traceplots). Function inputs, argument
syntax, and output format are nearly identical to the
'R2WinBUGS'/'R2OpenBUGS' packages to allow easy switching between MCMC
samplers.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
