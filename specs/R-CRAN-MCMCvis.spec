%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MCMCvis
%global packver   0.16.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Visualize, Manipulate, and Summarize MCMC Output

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-overlapping 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rstan 
Requires:         R-methods 
Requires:         R-CRAN-overlapping 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-rstantools

%description
Performs key functions for MCMC analysis using minimal code - visualizes,
manipulates, and summarizes MCMC output. Functions support simple and
straightforward subsetting of model parameters within the calls, and
produce presentable and 'publication-ready' output. MCMC output may be
derived from Bayesian model output fit with Stan, NIMBLE, JAGS, and other
software.

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
