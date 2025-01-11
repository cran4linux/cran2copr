%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multilevelmediation
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Functions for Multilevel Mediation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-glmmTMB 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-glmmTMB 

%description
The ultimate goal is to support 2-2-1, 2-1-1, and 1-1-1 models for
multilevel mediation, the option of a moderating variable for either the
a, b, or both paths, and covariates. Currently the 1-1-1 model is
supported and several options of random effects; the initial code for
bootstrapping was evaluated in simulations by Falk, Vogel, Hammami, and
Miočević (2024) <doi:10.3758/s13428-023-02079-4>. Support for Bayesian
estimation using 'brms' comprises ongoing work. Currently only continuous
mediators and outcomes are supported. Factors for any predictors must be
numerically represented.

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
