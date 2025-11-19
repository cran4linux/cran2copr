%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UComp
%global packver   5.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Univariate Time Series Modelling of many Kinds

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-tsoutliers 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-tsoutliers 
Requires:         R-stats 
Requires:         R-CRAN-ggforce 
Requires:         R-utils 
Requires:         R-parallel 

%description
Comprehensive analysis and forecasting of univariate time series using
automatic time series models of many kinds. Harvey AC (1989)
<doi:10.1017/CBO9781107049994>. Pedregal DJ and Young PC (2002)
<doi:10.1002/9780470996430>. Durbin J and Koopman SJ (2012)
<doi:10.1093/acprof:oso/9780199641178.001.0001>. Hyndman RJ, Koehler AB,
Ord JK, and Snyder RD (2008) <doi:10.1007/978-3-540-71918-2>. Gómez V,
Maravall A (2000) <doi:10.1002/9781118032978>. Pedregal DJ, Trapero JR and
Holgado E (2024) <doi:10.1016/j.ijforecast.2023.09.004>.

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
