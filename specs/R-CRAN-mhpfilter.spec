%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mhpfilter
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modified Hodrick-Prescott Filter with Optimal Smoothing Parameter Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-collapse >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.12.0.0.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-collapse >= 2.0.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-RcppArmadillo >= 0.12.0.0.0

%description
High-performance implementation of the Modified Hodrick-Prescott (HP)
Filter for decomposing macroeconomic time series into trend and cyclical
components. Based on the methodology of Choudhary, Hanif and Iqbal (2014)
<doi:10.1080/00036846.2014.894631> "On smoothing macroeconomic time series
using the modified HP filter", which uses generalized cross-validation
(GCV) to automatically select the optimal smoothing parameter lambda,
following McDermott (1997) "An automatic method for choosing the smoothing
parameter in the HP filter" (as described in Coe and McDermott (1997)
<doi:10.2307/3867497>). Unlike the standard HP filter that uses fixed
lambda values (1600 for quarterly, 100 for annual data), this package
estimates series-specific lambda values that minimize the GCV criterion.
Implements efficient C++ routines via 'RcppArmadillo' for fast
computation, supports batch processing of multiple series, and provides
comprehensive visualization tools using 'ggplot2'. Particularly useful for
cross-country macroeconomic comparisons, business cycle analysis, and when
the appropriate smoothing parameter is uncertain.

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
