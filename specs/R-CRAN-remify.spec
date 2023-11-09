%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remify
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Processing and Transforming Relational Event History Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-igraph >= 1.4.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-igraph >= 1.4.3
Requires:         R-CRAN-Rcpp >= 1.0.8.3

%description
Efficiently processes relational event history data and transforms them
into formats suitable for other packages. The primary objective of this
package is to convert event history data into a format that integrates
with the packages in 'remverse' and is compatible with various analytical
tools (e.g., computing network statistics, estimating tie-oriented or
actor-oriented social network models). Second, it can also transform the
data into formats compatible with other packages out of 'remverse'. The
package processes the data for two types of temporal social network
models: tie-oriented modeling framework (Butts, C., 2008,
<doi:10.1111/j.1467-9531.2008.00203.x>) and actor-oriented modeling
framework (Stadtfeld, C., & Block, P., 2017, <doi:10.15195/v4.a14>).

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
