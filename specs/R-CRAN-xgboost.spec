%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xgboost
%global packver   1.7.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Gradient Boosting

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Matrix >= 1.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Matrix >= 1.1.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-methods 

%description
Extreme Gradient Boosting, which is an efficient implementation of the
gradient boosting framework from Chen & Guestrin (2016)
<doi:10.1145/2939672.2939785>. This package is its R interface. The
package includes efficient linear model solver and tree learning
algorithms. The package can automatically do parallel computation on a
single machine which could be more than 10 times faster than existing
gradient boosting packages. It supports various objective functions,
including regression, classification and ranking. The package is made to
be extensible, so that users are also allowed to define their own
objectives easily.

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
