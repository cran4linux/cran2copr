%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FARS
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Factor-Augmented Regression Scenarios

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-SyScSelection 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-SyScSelection 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 

%description
Provides a comprehensive framework in R for modeling and forecasting
economic scenarios based on multi-level dynamic factor model. The package
enables users to: (i) extract global and group-specific factors using a
flexible multi-level factor structure; (ii) compute asymptotically valid
confidence regions for the estimated factors, accounting for uncertainty
in the factor loadings; (iii) obtain estimates of the parameters of the
factor-augmented quantile regressions together with their standard
deviations; (iv) recover full predictive conditional densities from
estimated quantiles; (v) obtain risk measures based on extreme quantiles
of the conditional densities; (vi) estimate the conditional density and
the corresponding extreme quantiles when the factors are stressed.

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
