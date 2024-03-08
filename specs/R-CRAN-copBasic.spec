%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  copBasic
%global packver   2.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          General Bivariate Copula Theory and Many Utility Functions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lmomco 
BuildRequires:    R-CRAN-randtoolbox 
Requires:         R-CRAN-lmomco 
Requires:         R-CRAN-randtoolbox 

%description
Extensive functions for bivariate copula (bicopula) computations and
related operations for bicopula theory. The lower, upper, product, and
select other bicopula are implemented along with operations including the
diagonal, survival copula, dual of a copula, co-copula, and numerical
bicopula density. Level sets, horizontal and vertical sections are
supported. Numerical derivatives and inverses of a bicopula are provided
through which simulation is implemented. Bicopula composition, convex
combination, asymmetry extension, and products also are provided. Support
extends to the Kendall Function as well as the Lmoments thereof. Kendall
Tau, Spearman Rho and Footrule, Gini Gamma, Blomqvist Beta, Hoeffding Phi,
Schweizer- Wolff Sigma, tail dependency, tail order, skewness, and
bivariate Lmoments are implemented, and positive/negative quadrant
dependency, left (right) increasing (decreasing) are available. Other
features include Kullback-Leibler Divergence, Vuong Procedure, spectral
measure, and Lcomoments for inference, maximum likelihood, and AIC, BIC,
and RMSE for goodness-of-fit.

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
