%global __brp_check_rpaths %{nil}
%global packname  PortfolioEffectEstim
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          High Frequency Price Estimators by PortfolioEffect

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PortfolioEffectHFT >= 1.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-PortfolioEffectHFT >= 1.7
Requires:         R-methods 
Requires:         R-CRAN-rJava 

%description
R interface to PortfolioEffect cloud service for estimating high frequency
price variance, quarticity, microstructure noise variance, and other
metrics in both aggregate and rolling window flavors. Constructed
estimators could use client-side market data or access HF intraday price
history for all major US Equities. See <https://www.portfolioeffect.com/>
for more information on the PortfolioEffect high frequency portfolio
analytics platform.

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
