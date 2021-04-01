%global packname  BayesRGMM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Robust Generalized Mixed Models for Longitudinal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-batchmeans 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-batchmeans 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rdpack 

%description
To perform model estimation using MCMC algorithms with Bayesian methods
for incomplete longitudinal studies on binary outcomes that are measured
repeatedly on subjects over time with drop-outs. Details about the method
can be found in the vignette or
<https://sites.google.com/view/kuojunglee/r-packages/bayesrgmm>.

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
