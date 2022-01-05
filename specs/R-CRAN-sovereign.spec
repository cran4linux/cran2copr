%global __brp_check_rpaths %{nil}
%global packname  sovereign
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          State-Dependent Empirical Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
A set of tools for state-dependent empirical analysis through both VAR-
and local projection-based state-dependent forecasts, impulse response
functions, historical decompositions, and forecast error variance
decompositions.

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
