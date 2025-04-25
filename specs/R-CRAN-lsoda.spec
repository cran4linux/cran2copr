%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lsoda
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'C++' Header Library for Ordinary Differential Equations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-Rcpp >= 1.0.12

%description
A 'C++' header library for using the 'libsoda-cxx' library with R. The
'C++' header reimplements the 'lsoda' function from the 'ODEPACK' library
for solving initial value problems for first order ordinary differential
equations (Hindmarsh, 1982;
<https://computing.llnl.gov/sites/default/files/ODEPACK_pub1_u88007.pdf>).
The 'C++' header can be used by other R packages by linking against this
package. The 'C++' functions can be called inline using 'Rcpp'. Finally,
the package provides an 'ode' function to call from R.

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
