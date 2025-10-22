%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  testthatdocs
%global packver   1.0.23
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.23
Release:          1%{?dist}%{?buildtag}
Summary:          Automated and Idempotent Unit Tests Documentation for Reproducible Quality Assurance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch

%description
Automates documentation of test_that() calls within R test files. The
package scans test sources, extracts human-readable test titles (even when
composed with functions like paste() or glue::glue(), ... etc.), and
generates reproducible roxygen2-style listings that can be inserted both
globally and per-section. It ensures idempotent updates and supports
customizable numbering templates with hierarchical indices. Designed for
developers, QA teams, and package maintainers seeking consistent,
self-documenting test inventories.

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
