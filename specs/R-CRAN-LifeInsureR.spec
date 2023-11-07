%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LifeInsureR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Traditional Life Insurance Contracts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-MortalityTables 
BuildRequires:    R-CRAN-objectProperties 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-MortalityTables 
Requires:         R-CRAN-objectProperties 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-tidyr 

%description
R6 classes to model traditional life insurance contracts like annuities,
whole life insurances or endowments. Such life insurance contracts provide
a guaranteed interest and are not directly linked to the performance of a
particular investment vehicle, but they typically provide (discretionary)
profit participation. This package provides a framework to model such
contracts in a very generic (cash-flow-based) way and includes modelling
profit participation schemes, dynamic increases or more general contract
layers, as well as contract changes (like sum increases or premium
waivers). All relevant quantities like premium decomposition, reserves and
benefits over the whole contract period are calculated and potentially
exported to 'Excel'. Mortality rates are given using the 'MortalityTables'
package.

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
