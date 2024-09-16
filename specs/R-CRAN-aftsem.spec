%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aftsem
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Accelerated Failure Time Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-optimx 

%description
Implements several basic algorithms for estimating regression parameters
for semiparametric accelerated failure time (AFT) model. The main methods
are: Jin rank-based method (Jin (2003) <doi:10.1093/biomet/90.2.341>),
Heller’s estimating method (Heller (2012)
<doi:10.1198/016214506000001257>), Polynomial smoothed Gehan function
method (Chung (2013) <doi:10.1007/s11222-012-9333-9>), Buckley-James
method (Buckley (1979) <doi:10.2307/2335161>) and Jin`s improved least
squares method (Jin (2006) <doi:10.1093/biomet/93.1.147>). This package
can be used for modeling right-censored data and for comparing different
estimation algorithms.

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
