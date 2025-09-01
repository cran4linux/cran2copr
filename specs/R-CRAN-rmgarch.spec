%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmgarch
%global packver   1.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate GARCH Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-rugarch >= 1.4.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.34
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-spd 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-rugarch >= 1.4.7
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-Bessel 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-spd 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-corpcor 

%description
Feasible multivariate GARCH models including DCC, GO-GARCH and
Copula-GARCH.

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
