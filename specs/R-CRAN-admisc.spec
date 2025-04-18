%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  admisc
%global packver   0.38
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.38
Release:          1%{?dist}%{?buildtag}
Summary:          Adrian Dusa's Miscellaneous

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Contains functions used across packages 'DDIwR', 'QCA' and 'venn'.
Interprets and translates, factorizes and negates SOP - Sum of Products
expressions, for both binary and multi-value crisp sets, and extracts
information (set names, set values) from those expressions. Other
functions perform various other checks if possibly numeric (even if all
numbers reside in a character vector) and coerce to numeric, or check if
the numbers are whole. It also offers, among many others, a highly
versatile recoding routine and some more flexible alternatives to the base
functions 'with()' and 'within()'. SOP simplification functions in this
package use related minimization from package 'QCA', which is recommended
to be installed despite not being listed in the Imports field, due to
circular dependency issues.

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
