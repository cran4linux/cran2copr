%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FMCensSkewReg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Finite Mixture of Censored Regression Models with Skewed Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MomTrunc 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-mixsmsn 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MomTrunc 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-mixsmsn 

%description
Provides an implementation of finite mixture regression models for
censored data under four distributional families: Normal (FM-NCR), Student
t (FM-TCR), skew-Normal (FM-SNCR), and skew-t (FM-STCR). The package
enables flexible modeling of skewness and heavy tails often observed in
real-world data, while explicitly accounting for censoring. Functions are
included for parameter estimation via the Expectation-Maximization (EM)
algorithm, computation of standard errors, and model comparison criteria
such as the Akaike Information Criterion (AIC), the Bayesian Information
Criterion (BIC), and the Efficient Determination Criterion (EDC). The
underlying methodology is described in Park et al. (2024)
<doi:10.1007/s00180-024-01459-4>.

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
