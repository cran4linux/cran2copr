%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AssetAllocation
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Backtesting Simple Asset Allocation Strategies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-RiskPortfolios 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-CRAN-riskParityPortfolio 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-RiskPortfolios 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-NMOF 
Requires:         R-CRAN-riskParityPortfolio 
Requires:         R-CRAN-curl 

%description
Easy and quick testing of customizable asset allocation strategies. Users
can rely on their own data, or have the package automatically download
data from Yahoo Finance (<https://finance.yahoo.com/>). Several pre-loaded
portfolios with data are available, including some which are discussed in
Faber (2015, ISBN:9780988679924).

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
