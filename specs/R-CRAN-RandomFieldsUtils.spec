%global __brp_check_rpaths %{nil}
%global packname  RandomFieldsUtils
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for the Simulation and Analysis of Random Fields and Genomic Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-parallel 

%description
Various utilities are provided that might be used in spatial statistics
and elsewhere. It delivers a method for solving linear equations that
checks the sparsity of the matrix before any algorithm is used. In
particular the following algorithms are implemented: the pivoted Cholesky
decomposition <doi:10.1016/j.apnum.2011.10.001> and on graphic cards, the
Struve functions <doi:10.1090/S0025-5718-1993-1176713-8>, and a precise
algorithm for evaluating the special covariance function.

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
