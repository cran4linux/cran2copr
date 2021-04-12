%global packname  RcppParallel
%global packver   5.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Programming Tools for 'Rcpp'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    tbb-devel
Requires:         tbb-devel
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2

%description
High level functions for parallel programming with 'Rcpp'. For example,
the 'parallelFor()' function can be used to convert the work of a standard
serial "for" loop into a parallel one and the 'parallelReduce()' function
can be used for accumulating aggregate or other values.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install
export TBB_INC=%{_includedir}/tbb
export TBB_LIB=%{_libdir}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
