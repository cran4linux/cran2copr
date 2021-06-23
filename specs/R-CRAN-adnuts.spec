%global __brp_check_rpaths %{nil}
%global packname  adnuts
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          No-U-Turn MCMC Sampling for 'ADMB' Models

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-snowfall >= 1.84.6.1
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-R2admb 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-snowfall >= 1.84.6.1
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-R2admb 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstantools

%description
Bayesian inference using the no-U-turn (NUTS) algorithm by Hoffman and
Gelman (2014) <https://www.jmlr.org/papers/v15/hoffman14a.html>. Designed
for 'AD Model Builder' ('ADMB') models, or when R functions for
log-density and log-density gradient are available, such as 'Template
Model Builder' models and other special cases. Functionality is similar to
'Stan', and the 'rstan' and 'shinystan' packages are used for diagnostics
and inference.

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
