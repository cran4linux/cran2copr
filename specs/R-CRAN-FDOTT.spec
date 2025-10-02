%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FDOTT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Transport Based Testing in Factorial Design

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-transport 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-rrapply 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-transport 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-rrapply 
Requires:         R-stats 
Requires:         R-methods 

%description
Perform optimal transport based tests in factorial designs as introduced
in Groppe et al. (2025) <doi:10.48550/arXiv.2509.13970> via the FDOTT()
function. These tests are inspired by ANOVA and its nonparametric
counterparts. They allow for testing linear relationships in factorial
designs between finitely supported probability measures on a metric space.
Such relationships include equality of all measures (no treatment effect),
interaction effects between a number of factors, as well as main and
simple factor effects.

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
