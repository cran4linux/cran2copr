%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mirtCAT
%global packver   1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Computerized Adaptive Testing with Multidimensional Item Response Theory

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mirt >= 1.37
BuildRequires:    R-CRAN-shiny >= 1.0.1
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mirt >= 1.37
Requires:         R-CRAN-shiny >= 1.0.1
Requires:         R-CRAN-lattice 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-lpSolve 

%description
Provides tools to generate HTML interfaces for adaptive and non-adaptive
tests using the shiny package (Chalmers (2016)
<doi:10.18637/jss.v071.i05>). Suitable for applying unidimensional and
multidimensional computerized adaptive tests (CAT) using item response
theory methodology and for creating simple questionnaires forms to collect
response data directly in R. Additionally, optimal test designs (e.g.,
"shadow testing") are supported for tests that contain a large number of
item selection constraints. Finally, package contains tools useful for
performing Monte Carlo simulations for studying test item banks.

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
