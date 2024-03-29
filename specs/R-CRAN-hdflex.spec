%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdflex
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Aggregate Density Forecasts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-parallel >= 4.3.0
BuildRequires:    R-stats >= 4.3.0
BuildRequires:    R-CRAN-checkmate >= 2.3.1
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-roll >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-parallel >= 4.3.0
Requires:         R-stats >= 4.3.0
Requires:         R-CRAN-checkmate >= 2.3.1
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-roll >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-Rcpp 

%description
Provides a forecasting method that maps vast numbers of (scalar-valued)
signals of any type into an aggregate density forecast in a time-varying
and computationally fast manner. The method proceeds in two steps: First,
it transforms a predictive signal into a density forecast. Second, it
combines the generated candidate density forecasts into an ultimate
density forecast. The methods are explained in detail in Adaemmer et al.
(2023) <doi:10.2139/ssrn.4342487>.

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
