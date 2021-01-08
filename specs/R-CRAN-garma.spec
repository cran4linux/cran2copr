%global packname  garma
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting and Forecasting Gegenbauer ARMA Time Series Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-FKF 
BuildRequires:    R-CRAN-tswge 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-crayon 
Requires:         R-utils 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-FKF 
Requires:         R-CRAN-tswge 

%description
Methods for estimating univariate long memory-seasonal/cyclical Gegenbauer
time series processes. See for example (2018) <doi:10.1214/18-STS649>.
Refer to the vignette for details of fitting these processes.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
