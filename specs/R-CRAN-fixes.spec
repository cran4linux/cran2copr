%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fixes
%global packver   0.11.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.2
Release:          1%{?dist}%{?buildtag}
Summary:          Staggered DiD Tools: Event Studies and ATT Aggregation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 

%description
Provides tools for difference-in-differences (DiD) estimation and
visualization with staggered adoption. Includes run_es() for event-study
curves (dynamic effects by relative time) and calc_att() for aggregated
ATT estimation (overall, by cohort, by calendar time). Supports multiple
modern estimators: Callaway-Sant'Anna (2021), Sun-Abraham (2021),
Borusyak-Jaravel-Spiess (2024), Wooldridge TWM, and Deb et al. FLEX.

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
