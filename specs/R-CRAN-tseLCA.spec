%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tseLCA
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Three-Step Estimation for Latent Class Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-multilevLCA 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-multilevLCA 

%description
Bias-adjusted three-step estimation of latent class models with covariates
and distal outcomes. The latent class measurement model is estimated
first, with 'multilevLCA' (Lyrvall et al., 2025)
<doi:10.1080/00273171.2025.2473935>, and held fixed; observations are then
classified; and the classes are related to covariates and distal outcomes
with the maximum likelihood correction of Vermunt (2010)
<doi:10.1093/pan/mpq025> and Bakk, Tekle and Vermunt (2013)
<doi:10.1177/0081175012470644>, or the correction of Bolck, Croon and
Hagenaars (2004) <doi:10.1093/pan/mph001>. Standard errors account for the
uncertainty of the measurement model (Bakk, Oberski and Vermunt, 2014)
<doi:10.1093/pan/mpu003>. Includes class enumeration, modal and
proportional class assignment, covariate formulas, Gaussian, Poisson,
binomial, and multinomial distal outcomes, the two-step estimator of Bakk
and Kuha (2018) <doi:10.1007/s11336-017-9592-7>, measurement models
applied to new samples, and full-information maximum likelihood for
missing indicators, standard methods for fitted models, and a
data-generating process replicating the simulation design of Bakk and Kuha
(2018).

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
