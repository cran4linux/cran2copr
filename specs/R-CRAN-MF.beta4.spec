%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MF.beta4
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring Ecosystem Multi-Functionality and Its Decomposition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-tidyverse 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-ggpubr 
Requires:         R-grid 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-tidyverse 

%description
Provide simple functions to (i) compute a class of multi-functionality
measures for a single ecosystem for given function weights, (ii) decompose
gamma multi-functionality for multiple ecosystems into a within-ecosystem
component (alpha multi-functionality) and an among-ecosystem component
(beta multi-functionality). In each case, the correlation between
functions can be corrected for. Based on biodiversity and ecosystem
function data, this software also facilitates graphics for assessing
biodiversity-ecosystem functioning relationships across scales.

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
