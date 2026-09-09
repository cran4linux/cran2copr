%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPrivStats
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differentially Private Classical Statistical Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 

%description
Implements differentially private (DP) versions of common classical
statistical procedures, including descriptive statistics (mean, variance,
quantiles, histograms), hypothesis tests (t-test, chi-square,
Kolmogorov-Smirnov, one-way ANOVA), and regression (closed-form DP linear
regression and DP-SGD for generalized linear models). Provides Laplace and
Gaussian mechanisms with analytic calibration, exponential mechanism for
medians, privacy-aware confidence intervals that account for both sampling
and privacy noise, and privacy budget accounting via basic, advanced, and
Renyi differential privacy (RDP) composition. Designed for official
statistics and privacy-preserving data analysis research.

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
