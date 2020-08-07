%global packname  garma
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Fitting and Forecasting Gegenbauer ARMA Time Series Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-FKF 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-FKF 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-ggplot2 

%description
Methods for estimating long memory-seasonal/cyclical Gegenbauer univariate
time series processes. See for example (2018) <doi:10.1214/18-STS649>.
Refer to the vignette for details of fitting these processes.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
