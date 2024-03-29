%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  highfrequency
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Highfrequency Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-Rcpp 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rsolnp 

%description
Provide functionality to manage, clean and match highfrequency trades and
quotes data, calculate various liquidity measures, estimate and forecast
volatility, detect price jumps and investigate microstructure noise and
intraday periodicity. A detailed vignette can be found in the open-access
paper "Analyzing Intraday Financial Data in R: The highfrequency Package"
by Boudt, Kleen, and Sjoerup (2022, <doi:10.18637/jss.v104.i08>).

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
