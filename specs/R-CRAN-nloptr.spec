%global __brp_check_rpaths %{nil}
%global packname  nloptr
%global packver   1.2.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to NLopt

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Solve optimization problems using an R interface to NLopt. NLopt is a
free/open-source library for nonlinear optimization, providing a common
interface for a number of different free optimization routines available
online as well as original implementations of various other algorithms.
See <http://ab-initio.mit.edu/wiki/index.php/NLopt_Introduction> for more
information on the available algorithms. During installation of nloptr on
Unix-based systems, the installer checks whether the NLopt library is
installed on the system. If the NLopt library cannot be found, the code is
compiled using the NLopt source included in the nloptr package.

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
