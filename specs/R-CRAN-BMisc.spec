%global __brp_check_rpaths %{nil}
%global packname  BMisc
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions for Panel Data, Quantiles, and Printing Results

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tidyr 

%description
These are miscellaneous functions for working with panel data, quantiles,
and printing results.  For panel data, the package includes functions for
making a panel data balanced (that is, dropping missing individuals that
have missing observations in any time period), converting id numbers to
row numbers, and to treat repeated cross sections as panel data under the
assumption of rank invariance.  For quantiles, there are functions to make
distribution functions from a set of data points (this is particularly
useful when a distribution function is created in several steps), to
combine distribution functions based on some external weights, and to
invert distribution functions.  Finally, there are several other
miscellaneous functions for obtaining weighted means, weighted
distribution functions, and weighted quantiles; to generate summary
statistics and their differences for two groups; and to add or drop
covariates from formulas.

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
