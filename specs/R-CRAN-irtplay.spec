%global __brp_check_rpaths %{nil}
%global packname  irtplay
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Unidimensional Item Response Theory Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 

%description
Fit unidimensional item response theory (IRT) models to a mixture of
dichotomous and polytomous data, calibrate online item parameters (i.e.,
pretest and operational items), estimate examinees' abilities, and examine
the IRT model-data fit on item-level in different ways as well as provide
useful functions related to unidimensional IRT models. For the item
parameter estimation, marginal maximum likelihood estimation via
expectation-maximization (MMLE-EM) algorithm (Bock & Aitkin (1981)
<doi:10.1007/BF02294168>) is used. For the online calibration, the fixed
item parameter calibration method (Kim (2006)
<doi:10.1111/j.1745-3984.2006.00021.x>) and the fixed ability parameter
calibration method (Ban, Hanson, Wang, Yi, & Harris (2011)
<doi:10.1111/j.1745-3984.2001.tb01123.x>) are provided. For the ability
estimation, several popular scoring methods (e.g., MLE, EAP, and MAP) are
implemented. In terms of assessing the IRT model-data fit, one of
distinguished features of this package is that it gives not only
well-known item fit statistics (e.g., chi-square (X2), likelihood ratio
chi-square (G2), infit and oufit statistics, and S-X2 statistic (Ames &
Penfield (2015) <doi:10.1111/emip.12067>)) but also graphical displays to
look at residuals between the observed data and model-based predictions
(Hambleton, Swaminathan, & Rogers (1991, ISBN:9780803936478)). In
addition, there are many useful functions such as analyzing differential
item functioning, computing asymptotic variance-covariance matrices of
item parameter estimates (Li & Lissitz (2004)
<doi:10.1111/j.1745-3984.2004.tb01109.x>), importing item and/or ability
parameters from popular IRT software, running 'flexMIRT' (Cai, 2017)
through R, generating simulated data, computing the conditional
distribution of observed scores using the Lord-Wingersky recursion formula
(Lord & Wingersky (1984) <doi:10.1177/014662168400800409>), computing the
loglikelihood of individual items, computing the loglikelihood of
abilities, computing item and test information functions, computing item
and test characteristic curve functions, and plotting item and test
characteristic curves and item and test information functions.

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
