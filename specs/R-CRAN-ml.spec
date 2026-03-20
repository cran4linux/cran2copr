%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ml
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Supervised Learning with Mandatory Splits and Seeds

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Implements the split-fit-evaluate-assess workflow from Hastie, Tibshirani,
and Friedman (2009, ISBN:978-0-387-84857-0) "The Elements of Statistical
Learning", Chapter 7. Provides three-way data splitting with automatic
stratification, mandatory seeds for reproducibility, automatic data type
handling, and 10 algorithms out of the box. Uses 'Rust' backend for
cross-language deterministic splitting. Designed for tabular supervised
learning with minimal ceremony. Polyglot parity with the 'Python' 'mlw'
package on 'PyPI'.

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
