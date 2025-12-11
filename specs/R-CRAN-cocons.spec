%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cocons
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate-Based Covariance Functions for Nonstationary Spatial Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spam >= 2.9.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-spam >= 2.9.1
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-fields 
Requires:         R-CRAN-optimParallel 
Requires:         R-methods 
Requires:         R-CRAN-knitr 

%description
Estimation, prediction, and simulation of nonstationary Gaussian process
with modular covariate-based covariance functions. Sources of
nonstationarity, such as spatial mean, variance, geometric anisotropy,
smoothness, and nugget, can be considered based on spatial
characteristics. An induced compact-supported nonstationary covariance
function is provided, enabling fast and memory-efficient computations when
handling densely sampled domains.

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
