%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StatMatch
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Matching or Data Fusion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 

%description
Integration of two data sources referred to the same target population
which share a number of variables. Some functions can also be used to
impute missing values in data sets through hot deck imputation methods.
Methods to perform statistical matching when dealing with data from
complex sample surveys are available too.

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
