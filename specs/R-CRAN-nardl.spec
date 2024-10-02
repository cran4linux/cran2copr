%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nardl
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Cointegrating Autoregressive Distributed Lag Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-car 
Requires:         R-CRAN-MASS 

%description
Computes the nonlinear cointegrating autoregressive distributed lag model
with automatic bases aic and bic lags selection of independent variables
proposed by (Shin, Yu & Greenwood-Nimmo, 2014
<doi:10.1007/978-1-4899-8008-3_9>).

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
