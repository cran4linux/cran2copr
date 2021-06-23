%global __brp_check_rpaths %{nil}
%global packname  dfphase1
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Phase I Control Charts (with Emphasis on Distribution-Free Methods)

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-robustbase 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-robustbase 

%description
Statistical methods for retrospectively detecting changes in location
and/or dispersion of univariate and multivariate variables. Data values
are assumed to be independent, can be individual (one observation at each
instant of time) or subgrouped (more than one observation at each instant
of time). Control limits are computed, often using a permutation approach,
so that a prescribed false alarm probability is guaranteed without making
any parametric assumptions on the stable (in-control) distribution. See G.
Capizzi and G. Masarotto (2018) <doi:10.1007/978-3-319-75295-2> for an
introduction to the package.

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

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
