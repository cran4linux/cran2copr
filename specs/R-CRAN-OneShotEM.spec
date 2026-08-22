%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OneShotEM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient eM-Algorithm for One-Shot Device Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
Implements the simple and efficient Expectation-Maximization (eM)
algorithm proposed by Zhu, Li, Li, and Balakrishnan (2026)
<doi:10.1080/03610918.2025.2515193> for parameter estimation in one-shot
device accelerated life testing (ALT) data. Unlike traditional EM
algorithms that impute exact failure times, this method treats failure
counts between inspection intervals as missing data, resulting in faster
convergence and enhanced numerical stability. Supports Exponential,
Weibull, Lognormal, Gamma, and custom user-defined lifetime distributions
under log-linear stress models. Standard errors, confidence intervals,
model selection statistics (AIC, BIC, AICc, HQIC), residual diagnostics,
and visualization tools are provided. References: Balakrishnan and Ling
(2012) <doi:10.1016/j.csda.2011.09.010>, Fan, Balakrishnan, and Chang
(2009) <doi:10.1080/00949650802142592>.

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
