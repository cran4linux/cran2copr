%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcmsupply
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Public and Private Sector Contraceptive Market Supply Shares

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-tidybayes 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-tidybayes 
Requires:         R-CRAN-runjags 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Family Planning programs and initiatives typically use nationally
representative surveys to estimate key indicators of a country’s family
planning progress. However, in recent years, routinely collected family
planning services data (Service Statistics) have been used as a
supplementary data source to bridge gaps in the surveys. The use of
service statistics comes with the caveat that adjustments need to be made
for missing private sector contributions to the contraceptive method
supply chain. Evaluating the supply source of modern contraceptives often
relies on Demographic Health Surveys (DHS), where many countries do not
have recent data beyond 2015/16. Fortunately, in the absence of recent
surveys we can rely on statistical model-based estimates and projections
to fill the knowledge gap. We present a Bayesian, hierarchical,
penalized-spline model with multivariate-normal spline coefficients, to
account for across method correlations, to produce country-specific,annual
estimates for the proportion of modern contraceptive methods coming from
the public and private sectors. This package provides a quick and
convenient way for users to access the DHS modern contraceptive supply
share data at national and subnational administration levels, estimate,
evaluate and plot annual estimates with uncertainty for a sample of low-
and middle-income countries. Methods for the estimation of method supply
shares at the national level are described in Comiskey, Alkema, Cahill
(2022) <arXiv:2212.03844>.

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
