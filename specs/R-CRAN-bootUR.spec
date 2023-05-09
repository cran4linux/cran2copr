%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bootUR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Unit Root Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-parallelly 

%description
Set of functions to perform various bootstrap unit root tests for both
individual time series (including augmented Dickey-Fuller test and union
tests), multiple time series and panel data; see Smeekes and Wilms (2023)
<doi:10.18637/jss.v106.i12>, Palm, Smeekes and Urbain (2008)
<doi:10.1111/j.1467-9892.2007.00565.x>, Palm, Smeekes and Urbain (2011)
<doi:10.1016/j.jeconom.2010.11.010>, Moon and Perron (2012)
<doi:10.1016/j.jeconom.2012.01.008>, Smeekes and Taylor (2012)
<doi:10.1017/S0266466611000387> and Smeekes (2015)
<doi:10.1111/jtsa.12110> for key references.

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
