%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  collapse
%global packver   1.8.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.9
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced and Fast Data Transformation

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
A C/C++ based package for advanced data transformation and statistical
computing in R that is extremely fast, class-agnostic, and programmer
friendly through a flexible and parsimonious syntax. It is well integrated
with base R, 'dplyr' / (grouped) 'tibble', 'data.table', 'sf', 'plm'
(panel-series and data frames), and non-destructively handles other matrix
or data frame based classes (like 'ts', 'xts' / 'zoo', 'tsibble', ...) ---
Key Features: --- (1) Advanced statistical programming: A full set of fast
statistical functions supporting grouped and weighted computations on
vectors, matrices and data frames. Fast and programmable grouping,
ordering, unique values/rows, factor generation and interactions. Fast and
flexible functions for data manipulation, data object conversions, and
memory efficient R programming. (2) Advanced aggregation: Fast and easy
multi-data-type, multi-function, weighted and parallelized data
aggregation. (3) Advanced transformations: Fast row/column arithmetic,
(grouped) replacing and sweeping out of statistics (by reference),
(grouped, weighted) scaling/standardizing, (higher-dimensional) between
(averaging) and (quasi-)within (demeaning) transformations, linear
prediction, model fitting and testing exclusion restrictions. (4) Advanced
time-computations: Fast and flexible indexed time series and panel data
classes. Fast (sequences of) lags/leads, and (lagged/leaded, iterated,
quasi-, log-) differences and (compounded) growth rates on (irregular)
time series and panels. Multivariate auto-, partial- and cross-correlation
functions for panel data. Panel data to (ts-)array conversions. (5) List
processing: Recursive list search, splitting, extraction/subsetting,
apply, and generalized row-binding / unlisting to data frame. (6) Advanced
data exploration: Fast (grouped, weighted, panel-decomposed) summary
statistics and descriptive tools.

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
