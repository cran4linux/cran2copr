%global packname  RcppParallel
%global packver   5.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Programming Tools for 'Rcpp'

License:          GPL-2
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
grep -B4 CXX11STD %{packname}/src/Makevars.in > %{packname}/src/Makevars.in.new
echo 'PKG_LIBS = -ltbb -ltbbmalloc' >> %{packname}/src/Makevars.in.new
mv %{packname}/src/Makevars.in.new %{packname}/src/Makevars.in
rm -rf %{packname}/src/tbb
sed -i '/tbbLdFlags <- fun/a return(paste0("-L", asBuildPath(dirname(tbbLibPath())), " -ltbb -ltbbmalloc"))' %{packname}/R/build.R
sed -i '/tbbLibPath <- fun/a return("%{_libdir}/libtbb.so.2")' %{packname}/R/build.R
# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install
export RCPP_PARALLEL_BACKEND=tinythread
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
ln -s %{_libdir} %{buildroot}%{rlibdir}/%{packname}/lib
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
