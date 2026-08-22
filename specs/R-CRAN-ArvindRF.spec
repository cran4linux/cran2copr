%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ArvindRF
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Forest Regression with Arvind Distribution Error Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-goftest 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements Random Forest regression under the Arvind distribution error
model. Provides core distribution functions (density, cumulative
distribution, quantile, random generation, hazard, survival), parameter
estimation via Expectation-Maximization (EM) and Markov Chain Monte Carlo
(MCMC), non-parametric bootstrap confidence intervals (at 90%%, 95%%, and
99%% levels), Highest Posterior Density (HPD) intervals, model evaluation
metrics (estimated values, bias, mean squared error, risk value),
homoscedastic prediction intervals, and goodness-of-fit diagnostic tests
(Kolmogorov-Smirnov and Anderson-Darling tests, Akaike Information
Criterion, and Bayesian Information Criterion). References: Breiman (2001)
<doi:10.1023/A:1010933404324>; Wright and Ziegler (2017)
<doi:10.18637/jss.v077.i01>.

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
