%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wqspt
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Permutation Test for Weighted Quantile Sum Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-gWQS 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-gWQS 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-cowplot 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-car 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-nnet 

%description
Implements a permutation test method for the weighted quantile sum (WQS)
regression, building off the 'gWQS' package (Renzetti et al.
<https://CRAN.R-project.org/package=gWQS>). Weighted quantile sum
regression is a statistical technique to evaluate the effect of complex
exposure mixtures on an outcome (Carrico et al. 2015
<doi:10.1007/s13253-014-0180-3>). The model features a statistical power
and Type I error (i.e., false positive) rate trade-off, as there is a
machine learning step to determine the weights that optimize the linear
model fit. This package provides an alternative method based on a
permutation test that should reliably allow for both high power and low
false positive rate when utilizing WQS regression (Day et al. 2022
<doi:10.1289/EHP10570>).

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
