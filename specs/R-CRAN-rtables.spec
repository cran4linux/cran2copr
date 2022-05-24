%global __brp_check_rpaths %{nil}
%global packname  rtables
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reporting Tables

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-formatters >= 0.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-grid 
Requires:         R-CRAN-formatters >= 0.3.0
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-htmltools 
Requires:         R-grid 

%description
Reporting tables often have structure that goes beyond simple rectangular
data. The 'rtables' package provides a framework for declaring complex
multi-level tabulations and then applying them to data. This framework
models both tabulation and the resulting tables as hierarchical, tree-like
objects which support sibling sub-tables, arbitrary splitting or grouping
of data in row and column dimensions, cells containing multiple values,
and the concept of contextual summary computations. A convenient pipe-able
interface is provided for declaring table layouts and the corresponding
computations, and then applying them to data.

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
