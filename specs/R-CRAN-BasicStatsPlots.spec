%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BasicStatsPlots
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Ready Data Visualization and Simple Statistical Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-broom.helpers >= 1.20.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-broom.helpers >= 1.20.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Creates publication-ready data visualizations using 'ggplot2', together
with tools for common simple statistical analyses (confidence intervals,
ANOVA, linear and generalized regression). The package provides common
chart types and analyses with built-in validation, customization options,
and publication-friendly themes.

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
