%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epizootic
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Explicit Population Models of Disease Transmission in Wildlife

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-raster >= 3.6
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-poems >= 1.1.0
BuildRequires:    R-CRAN-doParallel >= 1.0.16
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-raster >= 3.6
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-poems >= 1.1.0
Requires:         R-CRAN-doParallel >= 1.0.16
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-Rcpp 

%description
This extension of the pattern-oriented modeling framework of the 'poems'
package provides a collection of modules and functions customized for
modeling disease transmission on a population scale in a spatiotemporally
explicit manner. This includes seasonal time steps, dispersal functions
that track disease state of dispersers, results objects that store disease
states, and a population simulator that includes disease dynamics.

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
