%global __brp_check_rpaths %{nil}
%global packname  scModels
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Discrete Distribution Models to Count Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    mpfr-devel
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gamlss.dist 

%description
Provides functions for fitting discrete distribution models to count data.
Included are the Poisson, the negative binomial, the Poisson-inverse
gaussian and, most importantly, a new implementation of the Poisson-beta
distribution (density, distribution and quantile functions, and random
number generator) together with a needed new implementation of Kummer's
function (also: confluent hypergeometric function of the first kind).
Three different implementations of the Gillespie algorithm allow data
simulation based on the basic, switching or bursting mRNA generating
processes. Moreover, likelihood functions for four variants of each of the
three aforementioned distributions are also available. The variants
include one population and two population mixtures, both with and without
zero-inflation. The package depends on the 'MPFR' libraries
(<https://www.mpfr.org/>) which need to be installed separately (see
description at <https://github.com/fuchslab/scModels>). This package is
supplement to the paper "A mechanistic model for the negative binomial
distribution of single-cell mRNA counts" by Lisa Amrhein, Kumar Harsha and
Christiane Fuchs (2019) <doi:10.1101/657619> available on bioRxiv.

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
