%global __brp_check_rpaths %{nil}
%global packname  pollen
%global packver   0.82.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.82.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Aerobiological Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 

%description
Supports analysis of aerobiological data. Available features include
determination of pollen season limits, replacement of outliers (Kasprzyk
and Walanus (2014) <doi:10.1007/s10453-014-9332-8>), calculation of
growing degree days (Baskerville and Emin (1969) <doi:10.2307/1933912>),
and determination of the base temperature for growing degree days (Yang et
al. (1995) <doi:10.1016/0168-1923(94)02185-M).

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
