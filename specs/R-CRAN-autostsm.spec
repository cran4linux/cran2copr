%global packname  autostsm
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Structural Time Series Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-forecast >= 8.13
BuildRequires:    R-parallel >= 4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3
BuildRequires:    R-CRAN-imputeTS >= 3.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-lubridate >= 1.7
BuildRequires:    R-CRAN-strucchange >= 1.5
BuildRequires:    R-CRAN-foreach >= 1.5
BuildRequires:    R-CRAN-maxLik >= 1.4
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.13
BuildRequires:    R-CRAN-doSNOW >= 1.0
BuildRequires:    R-CRAN-tsutils >= 0.9
BuildRequires:    R-CRAN-lmtest >= 0.9
BuildRequires:    R-CRAN-seastests >= 0.14
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-forecast >= 8.13
Requires:         R-parallel >= 4.0
Requires:         R-CRAN-ggplot2 >= 3.3
Requires:         R-CRAN-imputeTS >= 3.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-lubridate >= 1.7
Requires:         R-CRAN-strucchange >= 1.5
Requires:         R-CRAN-foreach >= 1.5
Requires:         R-CRAN-maxLik >= 1.4
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-data.table >= 1.13
Requires:         R-CRAN-doSNOW >= 1.0
Requires:         R-CRAN-tsutils >= 0.9
Requires:         R-CRAN-lmtest >= 0.9
Requires:         R-CRAN-seastests >= 0.14

%description
Automatic model selection for structural time series decomposition into
trend, cycle, and seasonal components using the Kalman filter. See
Koopman, Siem Jan and Marius Ooms (2012) "Forecasting Economic Time Series
Using Unobserved Components Time Series Models
<doi:10.1093/oxfordhb/9780195398649.013.0006>.

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
