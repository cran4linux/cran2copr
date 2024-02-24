%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BalancedSampling
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Balanced and Spatially Balanced Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12

%description
Select balanced and spatially balanced probability samples in
multi-dimensional spaces with any prescribed inclusion probabilities. It
contains fast (C++ via Rcpp) implementations of the included sampling
methods. The local pivotal method by Grafström, Lundström and Schelin
(2012) <doi:10.1111/j.1541-0420.2011.01699.x> and spatially correlated
Poisson sampling by Grafström (2012) <doi:10.1016/j.jspi.2011.07.003> are
included. Also the cube method (for balanced sampling) and the local cube
method (for doubly balanced sampling) are included, see Grafström and
Tillé (2013) <doi:10.1002/env.2194>.

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
