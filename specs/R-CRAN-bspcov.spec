%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bspcov
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Sparse Estimation of a Covariance Matrix

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-CholWishart 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggmcmc 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-FinCovRegularization 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-CholWishart 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggmcmc 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-FinCovRegularization 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Bayesian estimations of a covariance matrix for multivariate normal data.
Assumes that the covariance matrix is sparse or band matrix and
positive-definite. Methods implemented include the beta-mixture shrinkage
prior (Lee et al. (2022) <doi:10.1016/j.jmva.2022.105067>), screened
beta-mixture prior (Lee et al. (2024) <doi:10.1214/24-BA1495>), and
post-processed posteriors for banded and sparse covariances (Lee et al.
(2023) <doi:10.1214/22-BA1333>; Lee and Lee (2023)
<doi:10.1016/j.jeconom.2023.105475>). This software has been developed
using funding supported by Basic Science Research Program through the
National Research Foundation of Korea ('NRF') funded by the Ministry of
Education ('RS-2023-00211979', 'NRF-2022R1A5A7033499',
'NRF-2020R1A4A1018207' and 'NRF-2020R1C1C1A01013338').

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
