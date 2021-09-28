%global __brp_check_rpaths %{nil}
%global packname  msm
%global packver   1.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-State Markov and Hidden Markov Models in Continuous Time

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-expm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-expm 

%description
Functions for fitting continuous-time Markov and hidden Markov multi-state
models to longitudinal data.  Designed for processes observed at arbitrary
times in continuous time (panel data) but some other observation schemes
are supported. Both Markov transition rates and the hidden Markov output
process can be modelled in terms of covariates, which may be constant or
piecewise-constant in time.

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
