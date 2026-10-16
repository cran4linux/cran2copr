%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ethnoecologyR
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Ethnoecology Analysis and Landscape Knowledge Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-ggalluvial 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-ggalluvial 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-rstantools

%description
A comprehensive toolkit for quantitative ethnoecology analysis and
landscape knowledge modeling. Implements core indices including Landscape
Use (LU), Cultural Importance in Ecology (CIE), Frequency of Citation
(FC), Fidelity Level (FL), Number of Uses (NU), and Cultural Value of
Ecolandscape (CVe). Provides visualization tools for chord diagrams,
alluvial plots, and radial plots, as well as Bayesian consensus modeling
and bootstrap resampling to support reproducible research in Local
Ecological Knowledge (LEK) and participatory land-use decision analysis.
Methods are based on Tardío and Pardo-de-Santayana (2008)
<doi:10.1007/s12231-007-9004-5>, Reyes-García et al. (2006)
<https://www.jstor.org/stable/4257061>, and Friedman et al. (1986)
<doi:10.1037/0022-3514.51.6.1173>.

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
