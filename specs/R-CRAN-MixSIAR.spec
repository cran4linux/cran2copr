%global __brp_check_rpaths %{nil}
%global packname  MixSIAR
%global packver   3.1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mixing Models in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-splancs >= 2.01.40
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-MCMCpack >= 1.4.2
BuildRequires:    R-CRAN-bayesplot >= 1.4.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1
BuildRequires:    R-CRAN-ggmcmc >= 1.1
BuildRequires:    R-CRAN-reshape >= 0.8.7
BuildRequires:    R-CRAN-R2jags >= 0.5.7
BuildRequires:    R-CRAN-lattice >= 0.20.35
BuildRequires:    R-CRAN-coda >= 0.19.1
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-splancs >= 2.01.40
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-MCMCpack >= 1.4.2
Requires:         R-CRAN-bayesplot >= 1.4.0
Requires:         R-CRAN-RColorBrewer >= 1.1
Requires:         R-CRAN-ggmcmc >= 1.1
Requires:         R-CRAN-reshape >= 0.8.7
Requires:         R-CRAN-R2jags >= 0.5.7
Requires:         R-CRAN-lattice >= 0.20.35
Requires:         R-CRAN-coda >= 0.19.1

%description
Creates and runs Bayesian mixing models to analyze biological tracer data
(i.e. stable isotopes, fatty acids), which estimate the proportions of
source (prey) contributions to a mixture (consumer). 'MixSIAR' is not one
model, but a framework that allows a user to create a mixing model based
on their data structure and research questions, via options for fixed/
random effects, source data types, priors, and error terms. 'MixSIAR'
incorporates several years of advances since 'MixSIR' and 'SIAR'.

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
