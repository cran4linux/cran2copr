%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tirt
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Testlet Item Response Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of Testlet Item Response Theory (tirt). A light-version yet
comprehensive and streamlined framework for psychometric analysis using
unidimensional Item Response Theory (IRT; Baker & Kim (2004)
<doi:10.1201/9781482276725>) and Testlet Response Theory (TRT; Wainer et
al., (2007) <doi:10.1017/CBO9780511618765>). Designed for researchers,
this package supports the estimation of item and person parameters for a
wide variety of models, including binary (i.e., Rasch, 2-Parameter
Logistic, 3-Parameter Logistic) and polytomous (Partial Credit Model,
Generalized Partial Credit Model, Graded Response Model) formats. It also
supports the estimation of Testlet models (Rasch Testlet, 2-Parameter
Logistic Testlet, 3-Parameter Logistic Testlet, Bifactor, Partial Credit
Model Testlet, Graded Response), allowing users to account for local item
dependence in bundled items. A key feature is the specialized support for
combination use and joint estimation of item response model and testlet
response model in one calibration. Beyond standard estimation via Marginal
Maximum Likelihood with Expectation-Maximization (EM) or Joint Maximum
Likelihood, the package offers robust tools for scale linking and equating
(Mean-Mean, Mean-Sigma, Stocking-Lord) to ensure comparability across
mixed-format test forms. It also facilitates fixed-parameter calibration,
enabling users to estimate person abilities with known item parameters or
vice versa, which is essential for pre-equating studies and item bank
maintenance. Comprehensive data simulation functions are included to
generate synthetic datasets with complex structures, including mixed-model
blocks and specific testlet effects, aiding in methodological research and
study design validation. Researchers can try multiple simulation
situations.

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
