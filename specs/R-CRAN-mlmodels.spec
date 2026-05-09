%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlmodels
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Models and Tools for Estimation, Prediction, and Testing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-marginaleffects 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-marginaleffects 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Provides a collection of maximum likelihood estimators with a consistent
S3 interface. Supported models include Gaussian (linear and log-normal),
logit, probit, Poisson, negative binomial (NB1 and NB2), gamma, and beta
regression. A distinctive feature is flexible modeling of the scale
parameter (variance, dispersion, precision, or shape) alongside the
location/mean parameters. The package offers unified predict() methods,
multiple variance-covariance estimators (observed information, outer
product of gradients, robust/Huber-White, cluster-robust, bootstrap,
jackknife), and a full suite of hypothesis tests (Wald, likelihood ratio,
information matrix, Vuong, overdispersion, and goodness-of-fit). It is
fully compatible with 'marginaleffects' for post-estimation analysis.
Methods implemented include Cameron and Trivedi (1990)
<doi:10.1016/0304-4076(90)90014-K>, for Poisson overdispersion testing,
Manjon and Martinez (2014) <doi:10.1177/1536867X1401400406>, for
goodness-of-fit testing of count data models, Vuong (1989)
<doi:10.2307/1912557>, for non-nested likelihood ratio testing, and White
(1982) <doi:10.2307/1912526>, for information matrix tests.

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
