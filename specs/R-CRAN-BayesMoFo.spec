%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesMoFo
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mortality Forecasting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
Carry out Bayesian estimation and forecasting for a variety of stochastic
mortality models using vague prior distributions. Models supported include
numerous well-established approaches introduced in the actuarial and
demographic literature, such as the Lee-Carter (1992)
<doi:10.1080/01621459.1992.10475265>, the Cairns-Blake-Dowd (2009)
<doi:10.1080/10920277.2009.10597538>, the Li-Lee (2005)
<doi:10.1353/dem.2005.0021>, and the Plat (2009)
<doi:10.1016/j.insmatheco.2009.08.006> models. The package is designed to
analyse stratified mortality data structured as a 3-dimensional array of
dimensions p × A × T (strata × age × year). Stratification can represent
factors such as cause of death, country, deprivation level, sex,
geographic region, insurance product, marital status, socioeconomic group,
or smoking behavior. While the primary focus is on analysing stratified
data (p > 1), the package can also handle mortality data that are not
stratified (p = 1). Model selection via the Deviance Information Criterion
(DIC) is supported.

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
