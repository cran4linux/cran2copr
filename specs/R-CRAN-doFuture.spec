%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doFuture
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Use Foreach to Parallelize via the Future Framework

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-future >= 1.49.0
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-globals 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-future >= 1.49.0
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-globals 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-utils 

%description
The 'future' package provides a unifying parallelization framework for R
that supports many parallel and distributed backends
<doi:10.32614/RJ-2021-048>. The 'foreach' package provides a powerful API
for iterating over an R expression in parallel. The 'doFuture' package
brings the best of the two together. There are two alternative ways to use
this package. The recommended approach is to use 'y <- foreach(...)
%%dofuture%% { ... }', which does not require using 'registerDoFuture()' and
has many advantages over '%%dopar%%'. The alternative is the traditional
'foreach' approach by registering the 'foreach' adapter
'registerDoFuture()' and so that 'y <- foreach(...) %%dopar%% { ... }' runs
in parallelizes with the 'future' framework.

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
