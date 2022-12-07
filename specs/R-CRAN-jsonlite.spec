%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jsonlite
%global packver   1.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Simple and Robust JSON Parser and Generator for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
A reasonably fast JSON parser and generator, optimized for statistical
data and the web. Offers simple, flexible tools for working with JSON in
R, and is particularly powerful for building pipelines and interacting
with a web API. The implementation is based on the mapping described in
the vignette (Ooms, 2014). In addition to converting JSON data from/to R
objects, 'jsonlite' contains functions to stream, validate, and prettify
JSON data. The unit tests included with the package verify that all edge
cases are encoded and decoded consistently for use with dynamic data in
systems and applications.

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
