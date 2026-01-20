%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flexCountReg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of a Variety of Count Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-cureplots 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-broom 
Requires:         R-CRAN-cureplots 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-maxLik 
Requires:         R-methods 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
An implementation of multiple regression models for count data. These
include various forms of the negative binomial (NB-1, NB-2, NB-P,
generalized negative binomial, etc.), Poisson-Lognormal, other compound
Poisson distributions, the Generalized Waring model, etc. Information on
the different forms of the negative binomial are described by Greene
(2008) <doi:10.1016/j.econlet.2007.10.015>. For treatises on count models,
see Cameron and Trivedi (2013) <doi:10.1017/CBO9781139013567> and Hilbe
(2012) <doi:10.1017/CBO9780511973420>. For the implementation of
under-reporting in count models, see Wood et al. (2016)
<doi:10.1016/j.aap.2016.06.013>. For prediction methods in random
parameter models, see Wood and Gayah (2025)
<doi:10.1016/j.aap.2025.108147>. For estimating random parameters using
maximum simulated likelihood, see Greene and Hill (2010)
<doi:10.1108/S0731-9053(2010)26>; Gourieroux and Monfort (1996)
<doi:10.1093/0198774753.001.0001>; or Hensher et al. (2015)
<doi:10.1017/CBO9781316136232>.

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
