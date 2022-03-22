%global __brp_check_rpaths %{nil}
%global packname  Rfmtool
%global packver   4.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Fuzzy Measure Tools

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.2
Requires:         R-core >= 2.9.2

%description
Various tools for handling fuzzy measures, calculating Shapley value and
interaction index, Choquet and Sugeno integrals, as well as fitting fuzzy
measures to empirical data are provided. Construction of fuzzy measures
from empirical data is done by solving a linear programming problem by
using 'lpsolve' package, whose source in C adapted to the R environment is
included. The description of the basic theory of fuzzy measures is in the
manual in the Doc folder in this package. Please refer to the following:
[1] <https://personal-sites.deakin.edu.au/~gleb/fmtools.html> [2] G.
Beliakov, H. Bustince, T. Calvo, 'A Practical Guide to Averaging',
Springer, (2016, ISBN: 978-3-319-24753-3). [3] G. Beliakov, S. James, J-Z.
Wu, 'Discrete Fuzzy Measures', Springer, (2020, ISBN: 978-3-030-15305-2).

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
