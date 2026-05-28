%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icomb
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasting Hierarchical Time Series Using Information Combination

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fabletools >= 0.7.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-fabletools >= 0.7.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-vctrs 

%description
Implements the Information Combination (IComb) approach proposed by
Nguyen, Vahid and Wickramasuriya
(2025)<https://www.monash.edu/business/ebs/research/publications/ebs/2025/wp11-2025.pdf>
for hierarchical forecast reconciliation. The method combines information
from base forecasts constructed using different information sets while
ensuring coherence. It is implemented using a penalized regression-based
framework.

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
