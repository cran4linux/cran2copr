%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  repeated
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Normal Repeated Measurements Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.4
Requires:         R-core >= 1.4
BuildRequires:    R-CRAN-rmutil 
Requires:         R-CRAN-rmutil 

%description
Various functions to fit models for non-normal repeated measurements, such
as Binary Random Effects Models with Two Levels of Nesting, Bivariate
Beta-binomial Regression Models, Marginal Bivariate Binomial Regression
Models, Cormack capture-recapture models, Continuous-time Hidden Markov
Chain Models, Discrete-time Hidden Markov Chain Models, Changepoint
Location Models using a Continuous-time Two-state Hidden Markov Chain,
generalized nonlinear autoregression models, multivariate Gaussian copula
models, generalized non-linear mixed models with one random effect,
generalized non-linear mixed models using h-likelihood for one random
effect, Repeated Measurements Models for Counts with Frailty or Serial
Dependence, Repeated Measurements Models for Continuous Variables with
Frailty or Serial Dependence, Ordinal Random Effects Models with Dropouts,
marginal homogeneity models for square contingency tables, correlated
negative binomial models with Kalman update. References include Lindsey's
text books, JK Lindsey (2001) <isbn-10:0198508123> and JK Lindsey (1999)
<isbn-10:0198505590>.

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
