%global __brp_check_rpaths %{nil}
%global packname  quarks
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Methods for Calculating and Backtesting Value at Risk and Expected Shortfall

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-smoots 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-smoots 
Requires:         R-stats 

%description
Enables the user to calculate Value at Risk (VaR) and Expected Shortfall
(ES) by means of various types of historical simulation. Currently plain-,
age-, volatility-weighted- and filtered historical simulation are
implemented in this package. Volatility weighting can be carried out via
an exponentially weighted moving average model (EWMA) or other GARCH-type
models. The performance can be assessed via Traffic Light Test, Coverage
Tests and Loss Functions. The methods of the package are described in
Gurrola-Perez, P. and Murphy, D. (2015)
<https://EconPapers.repec.org/RePEc:boe:boeewp:0525> as well as McNeil,
J., Frey, R., and Embrechts, P. (2015)
<https://ideas.repec.org/b/pup/pbooks/10496.html>.

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
