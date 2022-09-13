%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  m5
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'M5 Forecasting' Challenges Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-lubridate 

%description
Contains functions, which facilitate downloading, loading and preparing
data from 'M5 Forecasting' challenges (by 'University of Nicosia', hosted
on 'Kaggle'). The data itself is set of time series of different product
sales in 'Walmart'. The package also includes a ready-to-use built-in M5
subset named 'tiny_m5'. For detailed information about the challenges,
see: Makridakis, S. & Spiliotis, E. & Assimakopoulos, V. (2020).
<doi:10.1016/j.ijforecast.2021.10.009>.

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
