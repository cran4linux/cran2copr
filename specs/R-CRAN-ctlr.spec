%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctlr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Tolerance Limits for Assessing Agreement

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.60
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-sandwich >= 3.0.0
BuildRequires:    R-CRAN-lme4 >= 1.1.35
BuildRequires:    R-CRAN-binom >= 1.1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-mfp2 >= 1.0.1
BuildRequires:    R-CRAN-lmtest >= 0.9.40
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.60
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-sandwich >= 3.0.0
Requires:         R-CRAN-lme4 >= 1.1.35
Requires:         R-CRAN-binom >= 1.1.1.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-mfp2 >= 1.0.1
Requires:         R-CRAN-lmtest >= 0.9.40
Requires:         R-stats 
Requires:         R-utils 

%description
Implements clinical tolerance limits (CTL) methodology for assessing
agreement between two measurement methods. Estimates the true latent trait
using Best Linear Unbiased Predictors (BLUP), models bias and variance
components, and calculates overall and conditional agreement
probabilities. Provides visualization tools including tolerance limit
plots and conditional probability of agreement plots with confidence
bands. This package is based on methods described in Taffé (2016)
<doi:10.1177/0962280216666667>, Taffé (2019)
<doi:10.1177/0962280219844535>, and 'Stata' package Taffé (2025)
<doi:10.1177/1536867X251365501>.

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
