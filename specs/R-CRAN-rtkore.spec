%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtkore
%global packver   1.6.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.12
Release:          1%{?dist}%{?buildtag}
Summary:          'STK++' Core Library Integration to 'R' using 'Rcpp'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-inline 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-inline 

%description
'STK++' <http://www.stkpp.org> is a collection of C++ classes for
statistics, clustering, linear algebra, arrays (with an 'Eigen'-like API),
regression, dimension reduction, etc. The integration of the library to
'R' is using 'Rcpp'. The 'rtkore' package includes the header files from
the 'STK++' core library. All files contain only template classes and/or
inline functions. 'STK++' is licensed under the GNU LGPL version 2 or
later. 'rtkore' (the 'stkpp' integration into 'R') is licensed under the
GNU GPL version 2 or later. See file LICENSE.note for details.

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
