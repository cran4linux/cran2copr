%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spam
%global packver   2.10-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          SPArse Matrix

License:          LGPL-2 | BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-dotCall64 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-dotCall64 
Requires:         R-grid 
Requires:         R-methods 

%description
Set of functions for sparse matrix algebra. Differences with other sparse
matrix packages are: (1) we only support (essentially) one sparse matrix
format, (2) based on transparent and simple structure(s), (3) tailored for
MCMC calculations within G(M)RF. (4) and it is fast and scalable (with the
extension package spam64). Documentation about 'spam' is provided by
vignettes included in this package, see also Furrer and Sain (2010)
<doi:10.18637/jss.v036.i10>; see 'citation("spam")' for details.

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
