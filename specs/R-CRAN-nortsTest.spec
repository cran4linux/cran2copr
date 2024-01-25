%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nortsTest
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Normality of Stationary Process

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-uroot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-zoo 
Requires:         R-methods 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-uroot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-zoo 

%description
Despite that several tests for normality in stationary processes have been
proposed in the literature, consistent implementations of these tests in
programming languages are limited. Seven normality test are implemented.
The asymptotic Lobato & Velasco's, asymptotic Epps, Psaradakis and Vávra,
Lobato & Velasco's and Epps sieve bootstrap approximations, El bouch et
al., and the random projections tests for univariate stationary process.
Some other diagnostics such as, unit root test for stationarity, seasonal
tests for seasonality, and arch effect test for volatility; are also
performed. Additionally, the El bouch test performs normality tests for
bivariate time series. The package also offers residual diagnostic for
linear time series models developed in several packages.

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
