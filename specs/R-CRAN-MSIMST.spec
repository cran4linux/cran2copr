%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSIMST
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Monotonic Single-Index Regression Model with the Skew-T Likelihood

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-MASS >= 7.3.58.4
BuildRequires:    R-parallel >= 4.3.0
BuildRequires:    R-CRAN-Rdpack >= 2.6
BuildRequires:    R-CRAN-fields >= 15.2
BuildRequires:    R-CRAN-mvtnorm >= 1.2.4
BuildRequires:    R-CRAN-truncnorm >= 1.0.9
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.58.4
Requires:         R-parallel >= 4.3.0
Requires:         R-CRAN-Rdpack >= 2.6
Requires:         R-CRAN-fields >= 15.2
Requires:         R-CRAN-mvtnorm >= 1.2.4
Requires:         R-CRAN-truncnorm >= 1.0.9
Requires:         R-CRAN-Rcpp >= 1.0.12

%description
Incorporates a Bayesian monotonic single-index mixed-effect model with a
multivariate skew-t likelihood, specifically designed to handle survey
weights adjustments. Features include a simulation program and an
associated Gibbs sampler for model estimation. The single-index function
is constrained to be monotonic increasing, utilizing a customized Gaussian
process prior for precise estimation. The model assumes random effects
follow a canonical skew-t distribution, while residuals are represented by
a multivariate Student-t distribution. Offers robust Bayesian adjustments
to integrate survey weight information effectively.

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
