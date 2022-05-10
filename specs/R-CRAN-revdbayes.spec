%global __brp_check_rpaths %{nil}
%global packname  revdbayes
%global packver   1.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Ratio-of-Uniforms Sampling for Bayesian Extreme Value Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-rust >= 1.2.2
BuildRequires:    R-CRAN-bayesplot >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-exdex 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rust >= 1.2.2
Requires:         R-CRAN-bayesplot >= 1.1.0
Requires:         R-CRAN-exdex 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions for the Bayesian analysis of extreme value models.  The
'rust' package <https://cran.r-project.org/package=rust> is used to
simulate a random sample from the required posterior distribution. The
functionality of 'revdbayes' is similar to the 'evdbayes' package
<https://cran.r-project.org/package=evdbayes>, which uses Markov Chain
Monte Carlo ('MCMC') methods for posterior simulation.  In addition, there
are functions for making inferences about the extremal index, using the
models for threshold inter-exceedance times of Suveges and Davison (2010)
<doi:10.1214/09-AOAS292> and Holesovsky and Fusek (2020)
<doi:10.1007/s10687-020-00374-3>. Also provided are d,p,q,r functions for
the Generalised Extreme Value ('GEV') and Generalised Pareto ('GP')
distributions that deal appropriately with cases where the shape parameter
is very close to zero.

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
