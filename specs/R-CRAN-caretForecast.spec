%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  caretForecast
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conformal Time Series Forecasting Using State of Art Machine Learning Algorithms

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.15
BuildRequires:    R-CRAN-caret >= 6.0.88
BuildRequires:    R-methods >= 4.1.1
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-generics >= 0.1.3
Requires:         R-CRAN-forecast >= 8.15
Requires:         R-CRAN-caret >= 6.0.88
Requires:         R-methods >= 4.1.1
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-generics >= 0.1.3

%description
Conformal time series forecasting using the caret infrastructure. It
provides access to state-of-the-art machine learning models for
forecasting applications. The hyperparameter of each model is selected
based on time series cross-validation, and forecasting is done
recursively.

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
