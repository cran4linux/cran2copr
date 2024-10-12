%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsgarch
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate GARCH Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-TMB >= 1.7.20
BuildRequires:    R-CRAN-tsmethods >= 1.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tsdistributions 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.20
Requires:         R-CRAN-tsmethods >= 1.0.2
Requires:         R-methods 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-flextable 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tsdistributions 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-sandwich 

%description
Multiple flavors of the Generalized Autoregressive Conditional
Heteroskedasticity (GARCH) model with a large choice of conditional
distributions. Methods for specification, estimation, prediction,
filtering, simulation, statistical testing and more. Represents a partial
re-write and re-think of 'rugarch', making use of automatic
differentiation for estimation.

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
