%global packname  SpatMCA
%global packver   1.0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Spatial Maximum Covariance Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppParallel >= 0.11.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppParallel >= 0.11.2
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-MASS 

%description
Provide regularized maximum covariance analysis incorporating smoothness,
sparseness and orthogonality of couple patterns by using the alternating
direction method of multipliers algorithm. The method can be applied to
either regularly or irregularly spaced data, including 1D, 2D, and 3D
(Wang and Huang, 2017 <doi:10.1002/env.2481>).

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
