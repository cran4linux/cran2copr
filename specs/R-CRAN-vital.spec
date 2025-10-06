%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vital
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Analysis Tools for Mortality, Fertility, Migration and Population Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-HMDHFDplus >= 2.0.8
BuildRequires:    R-CRAN-fabletools >= 0.3.3
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-MortalityLaws 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-StMoMo 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-HMDHFDplus >= 2.0.8
Requires:         R-CRAN-fabletools >= 0.3.3
Requires:         R-CRAN-cobs 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-MortalityLaws 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-StMoMo 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-vctrs 

%description
Analysing vital statistics based on tools consistent with the tidyverse.
Tools are provided for data visualization, life table calculations,
computing net migration numbers, Lee-Carter modelling; functional data
modelling and forecasting.

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
