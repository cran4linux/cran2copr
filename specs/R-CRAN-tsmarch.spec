%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsmarch
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate ARCH Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-tsgarch >= 1.0.3
BuildRequires:    R-CRAN-tsmethods >= 1.0.2
BuildRequires:    R-CRAN-tsdistributions >= 1.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppBessel 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-tsgarch >= 1.0.3
Requires:         R-CRAN-tsmethods >= 1.0.2
Requires:         R-CRAN-tsdistributions >= 1.0.2
Requires:         R-methods 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RcppBessel 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 

%description
Feasible Multivariate Generalized Autoregressive Conditional
Heteroscedasticity (GARCH) models including Dynamic Conditional
Correlation (DCC), Copula GARCH and Generalized Orthogonal GARCH with
Generalized Hyperbolic distribution. A review of some of these models can
be found in Boudt, Galanos, Payseur and Zivot (2019)
<doi:10.1016/bs.host.2019.01.001>.

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
