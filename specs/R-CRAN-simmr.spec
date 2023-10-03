%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simmr
%global packver   0.5.1.214
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1.214
Release:          1%{?dist}%{?buildtag}
Summary:          A Stable Isotope Mixing Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-reshape2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-GGally 

%description
Fits Stable Isotope Mixing Models (SIMMs) and is meant as a longer term
replacement to the previous widely-used package SIAR. SIMMs are used to
infer dietary proportions of organisms consuming various food sources from
observations on the stable isotope values taken from the organisms' tissue
samples. However SIMMs can also be used in other scenarios, such as in
sediment mixing or the composition of fatty acids. The main functions are
simmr_load() and simmr_mcmc(). The two vignettes contain a quick start and
a full listing of all the features. The methods used are detailed in the
papers Parnell et al 2010 <doi:10.1371/journal.pone.0009672>, and Parnell
et al 2013 <doi:10.1002/env.2221>.

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
