%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sampbias
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluating Geographic Sampling Bias in Biological Collections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rnaturalearth 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rnaturalearth 

%description
Evaluating the biasing impact of geographic features such as airports,
cities, roads, rivers in datasets of coordinates based biological
collection datasets, by Bayesian estimation of the parameters of a Poisson
process. Enables also spatial visualization of sampling bias and includes
a set of convenience functions for publication level plotting. Also
available as 'shiny' app. The reference for the methodology is: Zizka et
al. (2020) <doi:10.1111/ecog.05102>.

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
