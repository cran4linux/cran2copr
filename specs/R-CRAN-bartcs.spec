%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bartcs
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Additive Regression Trees for Confounder Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-coda >= 0.4.0
BuildRequires:    R-CRAN-ggcharts 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda >= 0.4.0
Requires:         R-CRAN-ggcharts 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 

%description
Fit Bayesian Regression Additive Trees (BART) models to select true
confounders from a large set of potential confounders and to estimate
average treatment effect. For more information, see Kim et al. (2023)
<doi:10.1111/biom.13833>.

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
