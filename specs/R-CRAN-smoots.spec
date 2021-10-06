%global __brp_check_rpaths %{nil}
%global packname  smoots
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Estimation of the Trend and Its Derivatives in TS

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-future.apply >= 1.8.1
BuildRequires:    R-CRAN-future >= 1.22.1
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-progressr >= 0.8.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-future.apply >= 1.8.1
Requires:         R-CRAN-future >= 1.22.1
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-progressr >= 0.8.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
The nonparametric trend and its derivatives in equidistant time series
(TS) with short-memory stationary errors can be estimated. The estimation
is conducted via local polynomial regression using an automatically
selected bandwidth obtained by a built-in iterative plug-in algorithm or a
bandwidth fixed by the user. A Nadaraya-Watson kernel smoother is also
built-in as a comparison. With version 1.1.0, a linearity test for the
trend function, forecasting methods and backtesting approaches are
implemented as well. The smoothing methods of the package are described in
Feng, Y., Gries, T., and Fritz, M. (2020)
<doi:10.1080/10485252.2020.1759598>.

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
