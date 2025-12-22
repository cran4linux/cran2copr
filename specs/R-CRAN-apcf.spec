%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apcf
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Adapted Pair Correlation Function

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    geos-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-wk >= 0.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.12
Requires:         R-CRAN-wk >= 0.6.0
Requires:         R-CRAN-Rcpp >= 0.12

%description
The adapted pair correlation function transfers the concept of the pair
correlation function from point patterns to patterns of objects of finite
size and irregular shape (e.g. lakes within a country).  The pair
correlation function describes the spatial distribution of objects, e.g.
random, aggregated or regularly spaced. This is a reimplementation of the
method suggested by Nuske et al. (2009) <doi:10.1016/j.foreco.2009.09.050>
using the library 'GEOS' <doi:10.5281/zenodo.11396894>.

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
