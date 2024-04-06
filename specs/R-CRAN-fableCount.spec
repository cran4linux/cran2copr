%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fableCount
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          INGARCH and GLARMA Models for Count Time Series in Fable Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glarma >= 1.6.0
BuildRequires:    R-CRAN-tscount >= 1.4.3
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tsibble >= 0.9.0
BuildRequires:    R-CRAN-fable >= 0.3.4
BuildRequires:    R-CRAN-fabletools >= 0.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tsibbledata 
Requires:         R-CRAN-glarma >= 1.6.0
Requires:         R-CRAN-tscount >= 1.4.3
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tsibble >= 0.9.0
Requires:         R-CRAN-fable >= 0.3.4
Requires:         R-CRAN-fabletools >= 0.3.0
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tsibbledata 

%description
Provides a tidy R interface for count time series analysis. It includes
implementation of the INGARCH (Integer Generalized Autoregressive
Conditional Heteroskedasticity) model from the 'tscount' package and the
GLARMA (Generalized Linear Autoregressive Moving Averages) model from the
'glarma' package. Additionally, it offers automated parameter selection
algorithms based on the minimization of a penalized likelihood.

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
