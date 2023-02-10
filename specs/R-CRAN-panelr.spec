%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  panelr
%global packver   0.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Models and Utilities for Repeated Measures and Panel Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jtools >= 2.0.1
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-jtools >= 2.0.1
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 

%description
Provides an object type and associated tools for storing and wrangling
panel data. Implements several methods for creating regression models that
take advantage of the unique aspects of panel data. Among other
capabilities, automates the "within-between" (also known as
"between-within" and "hybrid") panel regression specification that
combines the desirable aspects of both fixed effects and random effects
econometric models and fits them as multilevel models (Allison, 2009
<doi:10.4135/9781412993869.d33>; Bell & Jones, 2015
<doi:10.1017/psrm.2014.7>). These models can also be estimated via
generalized estimating equations (GEE; McNeish, 2019
<doi:10.1080/00273171.2019.1602504>) and Bayesian estimation is
(optionally) supported via 'Stan'. Supports estimation of asymmetric
effects models via first differences (Allison, 2019
<doi:10.1177/2378023119826441>) as well as a generalized linear model
extension thereof using GEE.

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
