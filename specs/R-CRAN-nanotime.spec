%global __brp_check_rpaths %{nil}
%global packname  nanotime
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Nanosecond-Resolution Time Support for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppCCTZ >= 0.2.9
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppDate 
Requires:         R-CRAN-RcppCCTZ >= 0.2.9
Requires:         R-methods 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-zoo 

%description
Full 64-bit resolution date and time functionality with nanosecond
granularity is provided, with easy transition to and from the standard
'POSIXct' type. Three additional classes offer interval, period and
duration functionality for nanosecond-resolution timestamps.

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
