%global __brp_check_rpaths %{nil}
%global packname  RInside
%global packver   0.2.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.17
Release:          1%{?dist}%{?buildtag}
Summary:          C++ Classes to Embed R in C++ (and C) Applications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
C++ classes to embed R in C++ (and C) applications A C++ class providing
the R interpreter is offered by this package making it easier to have "R
inside" your C++ application. As R itself is embedded into your
application, a shared library build of R is required. This works on Linux,
OS X and even on Windows provided you use the same tools used to build R
itself. Numerous examples are provided in the nine subdirectories of the
examples/ directory of the installed package: standard, 'mpi' (for
parallel computing), 'qt' (showing how to embed 'RInside' inside a Qt GUI
application), 'wt' (showing how to build a "web-application" using the Wt
toolkit), 'armadillo' (for 'RInside' use with 'RcppArmadillo'), 'eigen'
(for 'RInside' use with 'RcppEigen'), and 'c_interface' for a basic C
interface and 'Ruby' illustration.  The examples use 'GNUmakefile(s)' with
GNU extensions, so a GNU make is required (and will use the 'GNUmakefile'
automatically). 'Doxygen'-generated documentation of the C++ classes is
available at the 'RInside' website as well.

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
