%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  collapse
%global packver   2.0.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.18
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced and Fast Data Transformation

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
A C/C++ based package for advanced data transformation and statistical
computing in R that is extremely fast, class-agnostic, robust and
programmer friendly. Core functionality includes a rich set of S3 generic
grouped and weighted statistical functions for vectors, matrices and data
frames, which provide efficient low-level vectorizations, OpenMP
multithreading, and skip missing values by default. These are integrated
with fast grouping and ordering algorithms (also callable from C), and
efficient data manipulation functions. The package also provides a
flexible and rigorous approach to time series and panel data in R. It
further includes fast functions for common statistical procedures,
detailed (grouped, weighted) summary statistics, powerful tools to work
with nested data, fast data object conversions, functions for memory
efficient R programming, and helpers to effectively deal with variable
labels, attributes, and missing data. It is well integrated with base R
classes, 'dplyr'/'tibble', 'data.table', 'sf', 'units', 'plm'
(panel-series and data frames), and 'xts'/'zoo'.

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
