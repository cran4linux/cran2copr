%global __brp_check_rpaths %{nil}
%global packname  LifeInsuranceContracts
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Framework for Traditional Life Insurance Contracts

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

%description
R6 classes to model traditional life insurance contracts like annuities,
whole life insurances or endowments. Such life insurance contracts provide
a guaranteed interest and are not directly linked to the performance of a
particular investment vehicle. However, they typically provide
(discretionary) profit participation. This package provides a framework to
model such contracts in a very generic (cash-flow-based) way and includes
modelling profit participation schemes, dynamic increases or more general
contract layers, as well as contract changes (like sum increases or
premium waivers). All relevant quantities like premium decomposition,
reserves and benefits over the whole contract period are calculated and
potentially exported to excel. Mortalities are given using the
'MortalityTables' package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
