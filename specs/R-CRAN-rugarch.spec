%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rugarch
%global packver   1.5-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate GARCH Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.34
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-spd 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-SkewHyperbolic 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-spd 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-SkewHyperbolic 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-graphics 
Requires:         R-CRAN-fracdiff 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-nloptr 

%description
ARFIMA, in-mean, external regressors and various GARCH flavors, with
methods for fit, forecast, simulation, inference and plotting.

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
