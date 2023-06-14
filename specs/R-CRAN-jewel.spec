%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jewel
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Models Estimation from Multiple Sources

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-SMUT 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-SMUT 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 

%description
Estimates networks of conditional dependencies (Gaussian graphical models)
from multiple classes of data (similar but not exactly, i.e. measurements
on different equipment, in different locations or for various sub-types).
Package also allows to generate simulation data and evaluate the
performance. Implementation of the method described in Angelini, De
Canditiis and Plaksienko (2022) <doi:10.3390/math10213983>.

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
