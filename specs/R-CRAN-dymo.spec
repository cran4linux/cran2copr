%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dymo
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Mode Decomposition for Multivariate Time Feature Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-imputeTS >= 3.2
BuildRequires:    R-CRAN-modeest >= 2.4.0
BuildRequires:    R-CRAN-readr >= 2.1.2
BuildRequires:    R-CRAN-lubridate >= 1.7.10
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-tictoc >= 1.0
BuildRequires:    R-CRAN-greybox >= 1.0.1
BuildRequires:    R-CRAN-matlib >= 0.9.5
BuildRequires:    R-CRAN-fANCOVA >= 0.6.1
BuildRequires:    R-CRAN-narray >= 0.4.1.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-moments >= 0.14
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-imputeTS >= 3.2
Requires:         R-CRAN-modeest >= 2.4.0
Requires:         R-CRAN-readr >= 2.1.2
Requires:         R-CRAN-lubridate >= 1.7.10
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-tictoc >= 1.0
Requires:         R-CRAN-greybox >= 1.0.1
Requires:         R-CRAN-matlib >= 0.9.5
Requires:         R-CRAN-fANCOVA >= 0.6.1
Requires:         R-CRAN-narray >= 0.4.1.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-moments >= 0.14

%description
An application of Dynamic Mode Decomposition for prediction of time
features. Automatic search for the best model across the space of all
possible feature combinations and ranks of Singular Value Decomposition.

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
