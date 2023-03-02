%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coda.base
%global packver   0.5.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Basic Set of Functions for Compositional Data Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-jsonlite 

%description
A minimum set of functions to perform compositional data analysis using
the log-ratio approach introduced by John Aitchison (1982). Main functions
have been implemented in c++ for better performance.

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
