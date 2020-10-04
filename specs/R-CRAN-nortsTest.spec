%global packname  nortsTest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Normality of Stationary Process

License:          LGPL
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
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-uroot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-zoo 
Requires:         R-methods 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-uroot 
Requires:         R-MASS 
Requires:         R-CRAN-zoo 

%description
Despite that several tests for normality in stationary processes have been
proposed in the literature, consistent implementations of these tests in
programming languages are limited. Four normality test are implemented.
The Lobato and Velasco's, Epps, Psaradakis and Vavra, and the random
projections tests for stationary process. Some other diagnostics such as,
unit root test for stationarity, seasonal tests for seasonality, and arch
effect test for volatility; are also performed. The package also offers
residual diagnostic for linear time series models developed in several
packages.

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
