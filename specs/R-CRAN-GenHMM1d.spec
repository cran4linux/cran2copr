%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GenHMM1d
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit for Zero-Inflated Univariate Hidden Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-VaRES 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-GLDEX 
BuildRequires:    R-CRAN-GeneralizedHyperbolic 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-sgt 
BuildRequires:    R-CRAN-skewt 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-ssdtools 
BuildRequires:    R-CRAN-stabledist 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-VaRES 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-GLDEX 
Requires:         R-CRAN-GeneralizedHyperbolic 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-sgt 
Requires:         R-CRAN-skewt 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-ssdtools 
Requires:         R-CRAN-stabledist 

%description
Inference, goodness-of-fit tests, and predictions for continuous and
discrete univariate Hidden Markov Models (HMM), including zero-inflated
distributions. The goodness-of-fit test is based on a Cramer-von Mises
statistic and uses parametric bootstrap to estimate the p-value. The
description of the methodology is taken from Nasri et al (2020)
<doi:10.1029/2019WR025122>.

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
