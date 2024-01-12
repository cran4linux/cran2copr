%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MPCR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi Precision Computing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-methods 

%description
Provides new data-structure support for multi- and mixed-precision for R
users. The package supports 16-bit, 32-bit, and 64-bit operations with the
ability to perform mixed-precision operations through a newly defined
tile-based data structure. To the best of our knowledge, 'MPCR' differs
from the currently available packages in the following: 'MPCR' introduces
a new data structure that supports three different precisions (16-bit,
32-bit, and 64-bit), allowing for optimized memory allocation based on the
desired precision. This feature offers significant advantages in-memory
optimization. 'MPCR' extends support to all basic linear algebra methods
across different precisions. 'MPCR' maintains a consistent interface with
normal R functions, allowing for seamless code integration and a
user-friendly experience. 'MPCR' also introduces support for the
tile-based matrix data structure with mixed precision, enabling the
utilization of a range of tile-based linear algebra algorithms.

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
