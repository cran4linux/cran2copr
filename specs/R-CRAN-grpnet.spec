%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  grpnet
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Group Elastic Net Regularized GLMs and GAMs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Efficient algorithms for fitting generalized linear and additive models
with group elastic net penalties as described in Helwig (2024)
<doi:10.1080/10618600.2024.2362232>. Implements group LASSO, group MCP,
and group SCAD with an optional group ridge penalty. Computes the
regularization path for linear regression (gaussian), multivariate
regression (multigaussian), logistic regression (binomial), multinomial
logistic regression (multinomial), log-linear count regression (poisson
and negative.binomial), and log-linear continuous regression (gamma and
inverse gaussian). Supports default and formula methods for model
specification, k-fold cross-validation for tuning the regularization
parameters, and nonparametric regression via tensor product reproducing
kernel (smoothing spline) basis function expansion.

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
