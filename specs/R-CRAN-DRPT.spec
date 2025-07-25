%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DRPT
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Density Ratio Permutation Test

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rdpack >= 2.6
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-Rdpack >= 2.6
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 

%description
Implementation of the Density Ratio Permutation Test for testing the
goodness-of-fit of a hypothesised ratio of two densities, as described in
Bordino and Berrett (2025) <doi:10.48550/arXiv.2505.24529>.

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
