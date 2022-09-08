%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SAEforest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Effect Random Forests for Small Area Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vip 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pdp 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-vip 

%description
Mixed Effects Random Forests (MERFs) are a data-driven, nonparametric
alternative to current methods of Small Area Estimation (SAE). 'SAEforest'
provides functions for the estimation of regionally disaggregated linear
and nonlinear indicators using survey sample data. Included procedures
facilitate the estimation of domain-level economic and inequality metrics
and assess associated uncertainty. Emphasis lies on straightforward
interpretation and visualization of results. From a methodological
perspective, the package builds on approaches discussed in Krennmair and
Schmid (2022) <arXiv:2201.10933v2> and Krennmair et al. (2022)
<arXiv:2204.10736>.

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
