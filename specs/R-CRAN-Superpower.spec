%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Superpower
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Power Analysis for Factorial Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-afex 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-afex 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 

%description
Functions to perform simulations of ANOVA designs of up to three factors.
Calculates the observed power and average observed effect size for all
main effects and interactions in the ANOVA, and all simple comparisons
between conditions. Includes functions for analytic power calculations and
additional helper functions that compute effect sizes for ANOVA designs,
observed error rates in the simulations, and functions to plot power
curves. Please see Lakens, D., & Caldwell, A. R. (2021). "Simulation-Based
Power Analysis for Factorial Analysis of Variance Designs".
<doi:10.1177/2515245920951503>.

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
