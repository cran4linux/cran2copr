%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  markets
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation Methods for Markets in Equilibrium and Disequilibrium

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-MASS >= 7.3.50
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-rlang >= 0.2.1
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppGSL 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.50
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppGSL 
Requires:         R-CRAN-RcppParallel 
Requires:         R-stats 

%description
Provides estimation methods for markets in equilibrium and disequilibrium.
Supports the estimation of an equilibrium and four disequilibrium models
with both correlated and independent shocks. Also provides post-estimation
analysis tools, such as aggregation, marginal effect, and shortage
calculations. See Karapanagiotis (2024) <doi:10.18637/jss.v108.i02> for an
overview of the functionality and examples. The estimation methods are
based on full information maximum likelihood techniques given in Maddala
and Nelson (1974) <doi:10.2307/1914215>. They are implemented using the
analytic derivative expressions calculated in Karapanagiotis (2020)
<doi:10.2139/ssrn.3525622>. Standard errors can be estimated by adjusting
for heteroscedasticity or clustering. The equilibrium estimation
constitutes a case of a system of linear, simultaneous equations. Instead,
the disequilibrium models replace the market-clearing condition with a
non-linear, short-side rule and allow for different specifications of
price dynamics.

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
